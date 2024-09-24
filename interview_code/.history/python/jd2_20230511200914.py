import torch
import torch.nn as nn
import torch.nn.functional as F
class FocalLoss(nn.Module):
    def __init__(self,alpha=1,gamma=2,reduction="mean"):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction
    
    def forward(self,inputs,target):
        BCE_Loss = F.binary_cross_entropy_with_logits(inputs,target)
        pt = torch.exp(BCE_Loss)#p_t = y*p + (1-y)*(1-p)
        F_loss = self.alpha*(1-pt)**self.gamma*BCE_Loss
        if self.reduction == "mean":
            return torch.mean(F_loss)
        elif self.reduction =="sum":
            return torch.sum(F_loss)
        else:
            return F_loss
        