import torch
import torch.nn as nn
import torch.nn.functional as F 	
#softmax((Q,K^T)/sqrt(d_k)V
def self_attention(Q,K,V): 
     
    ch,seq,dim = Q.size()
    score = torch.mm(Q,K.transpose(-2,-1)) 
    score = score/(dim**0.5)
    att = F.softmax(score,dim=-1)
    re =  torch.mm(att,V)  
    return re


    