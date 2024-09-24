# 哈佛的nlp课程 http://nlp.seas.harvard.edu/2018/04/03/attention.html#attention
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
def attention(query, key, value, mask=None, dropout=None):
    "Compute 'Scaled Dot Product Attention'"
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) \
             / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = F.softmax(scores, dim = -1)
    if dropout is not None:
        p_attn = dropout(p_attn)
    return torch.matmul(p_attn, value), p_attn
# self-attention 类  attention = softmax(QK^T/sqrt(d_k))V
class Attention_Layer(nn.Module):
    
    #用来实现mask-attention layer
    def __init__(self, hidden_dim):
        super(Attention_Layer,self).__init__()
        self.hidden_dim = hidden_dim
        
        self.Q_linear = nn.Linear(hidden_dim, hidden_dim, bias = False)
        self.K_linear = nn.Linear(hidden_dim, hidden_dim, bias = False)
        self.V_linear = nn.Linear(hidden_dim, hidden_dim, bias = False)
            
    def forward(self, inputs, mask):
        
        #计算生成QKV矩阵
        Q = self.Q_linear(inputs) 
        K = self.K_linear(inputs).permute(0, 2, 1)#先进行一次转置
        V = self.V_linear(inputs)
        
        alpha = torch.matmul(Q, K)/(self.hidden_dim**0.5)
        if mask is not None:
            alpha = alpha.masked_fill(mask, -1e9) #将mask的值忽略，造成影响不到计算
        alpha = F.softmax(alpha, dim = -1)
        out = torch.matmul(alpha, V)
        return out

#LayerNorm = alpha*(x-mean)/sqrt(std+eps) + beta
class LayerNorm(nn.Module):  #Attention_Layer的子类，也称为Attention_Block的子类。它的实现
    def __init__(self,features,eps) -> None:
        super(LayerNorm,self).__init__()
        self.a = nn.Parameter(torch.ones(features)) # σ的定义是在[0,1]之间的。也就是说，它们的
        self.b = nn.Parameter(torch.zeros(features)) # mean的定义是在0之间。也就是说，它们的mean和std
        self.eps = eps # small number to avoid dividing by zero （也称为NAN） （这在生产中不会成
    def forward(self,x):
        mean = x.mean(dim=-1,keepdim=True)
        std = x.std(dim=-1,keepdim=True)
        res = self.a*(x-mean)/(std+self.eps) + self.b
        return res
        
        
        
        
