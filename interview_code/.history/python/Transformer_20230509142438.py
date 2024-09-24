# 哈佛的nlp课程 http://nlp.seas.harvard.edu/2018/04/03/attention.html#attention
import torch
import torch.nn as nn
import torch.nn.functional as F

# self-attention 类
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
import copy
def clones(module, N):
    "Produce N identical layers."
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])
class EncoderLayer(nn.Module):
    "Encoder is made up of self-attn and feed forward (defined below)"
    def __init__(self, size, self_attn, feed_forward, dropout):
        super(EncoderLayer, self).__init__()
        self.self_attn = self_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 2)
        self.size = size

    def forward(self, x, mask):
        "Follow Figure 1 (left) for connections."
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, mask))
        return self.sublayer[1](x, self.feed_forward)   

class EncoderDecoder(nn.Module):
    """
    A standard Encoder-Decoder architecture. Base for this and many 
    other models.
    """
    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator
        
    def forward(self, src, tgt, src_mask, tgt_mask):
        "Take in and process masked src and target sequences."
        return self.decode(self.encode(src, src_mask), src_mask,
                            tgt, tgt_mask)
    
    def encode(self, src, src_mask):
        return self.encoder(self.src_embed(src), src_mask)
    
    def decode(self, memory, src_mask, tgt, tgt_mask):
        return self.decoder(self.tgt_embed(tgt), memory, src_mask, tgt_mask)
        
        
