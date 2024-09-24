import torch
import torch.nn as nn
import torch.nn.functional as F


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
        


        
        
