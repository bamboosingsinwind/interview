# 哈佛的nlp课程 http://nlp.seas.harvard.edu/2018/04/03/attention.html#attention
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import math

# self-attention 类  attention = softmax(QK^T/sqrt(d_k))V
class Attention_Layer(nn.Module):
    
    #用来实现mask-attention layer
    def __init__(self, hidden_dim):
        super(Attention_Layer,self).__init__()
        self.hidden_dim = hidden_dim
        
        self.Q_linear = nn.Linear(hidden_dim, hidden_dim, bias = False)
        self.K_linear = nn.Linear(hidden_dim, hidden_dim, bias = False)
        self.V_linear = nn.Linear(hidden_dim, hidden_dim, bias = False)
            
    def forward(self, inputs, mask):#inputs: [batch_size, seq_len, hidden_dim] 
        
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
def attention(query, key, value, mask=None, dropout=None):
    "Compute 'Scaled Dot Product Attention'"
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
             
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = F.softmax(scores, dim = -1)
    if dropout is not None:
        p_attn = dropout(p_attn)
    return torch.matmul(p_attn, value), p_attn
class MultiAttention(nn.Module):
    def __init__(self,h,d_model,dropout=0.1):
        super().__init__()
        self.d_k = d_model/h
        self.h  = h
        self.linears = nn.ModuleList([nn.Linear(d_model, d_model, bias = False) for _ in range(4)])
        self.att = None
        self.dropout = nn.Dropout(p=dropout)
    def forward(self,q,k,v,mask=None):#[batch_size,seq_len,head*d_k]  d_model = head*d_k
        if mask is not None:
            mask = mask.unsqueeze(1)
        bs = q.size(0)
        q,k,v = [l(x).view(bs, -1, self.h, self.d_k).transpose(1,2) for l,x in zip(self.linears, (q,k,v))]#[bs,seq_len,head,d_k]-->[bs,head,seq_len,d_k]
        x,self.att = attention(q,k,v,mask=mask,dropout=self.dropout)
        x = x.transpose(1,2).contiguous().view(bs, -1, self.h*self.d_k)# [bs,head,seq_len,d_k]-->[bs,seq_len,d_model]
        return self.linears[-1](x)
# PE(pos,2i)=sin(pos/10000^(2i/d_model))   i=0..d_model/2     PE(pos,2i+1)= cos(pos/10000^(2i/d_model))    
class PositionalEncoding(nn.Module):
    def __init__(self,d_model,dropout=0.1,maxlen=5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)  
        pe = torch.zeros(maxlen,d_model)  # [maxlen,d_model]  将数据维度维护为(max_len, d_model) 
        pos = torch.arange(0,maxlen).unsqueeze(1)  
        div = torch.exp(torch.arange(0,d_model,2) * (-math.log(10000.0)/d_model))# 1/10000^(2i/d_model)
        pe[:,0::2] =  torch.sin(pos * div)  # [maxlen,1] * [d_model//2]  
        pe[:,1::2] =  torch.cos(pos * div)
        pe = pe.unsqueeze(0) # [1,maxlen,d_model]  

        self.register_buffer("pe",pe)

    def forward(self,x):#[bs,seq_len]
        x = x + Variable(self.pe[:,:x.size(1)], requires_grad=False) 	
        return self.dropout(x)
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(15, 5))
pe = PositionalEncoding(20, 0)
y = pe.forward(Variable(torch.zeros(1, 100, 20)))
plt.plot(np.arange(100), y[0, :, 4:8].data.numpy())
plt.legend(["dim %d"%p for p in [4,5,6,7]])
None
        
        
        
class PoswiseFeedForward(nn.Module):#1D convolutional block for the position-wise feed forward NN. 描述：
    def __init__(self,d_model,d_ff,dropout=0.1):#d_model = head*d_k
        super().__init__()  #super().__init__() is the same as super(nn.Module, self).__init__() in Python
        self.w_1 = nn.Linear(d_model, d_ff)  #w_1 is the first linear transformation, a
        self.w_2 = nn.Linear(d_ff, d_model)  #w_2 is the second linear transformation, 
        self.dropout = nn.Dropout(dropout)  
    def forward(self,x):
        return self.w_2(self.dropout(F.relu(self.w_1(x)))) 


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
        
        
        
        
