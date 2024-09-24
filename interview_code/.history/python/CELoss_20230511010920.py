import torch
import torch.nn as nn
import torch.nn.functional as F 	# https://pytorch.org/docs/stable/nn.html#functional  https://pytorch
celoss = nn.CrossEntropyLoss(reduction="mean")
class myCELoss(nn.Module):   # 定义自己的损失函数类，继承nn.Module类 （这样它也可以被视为一个模块，便于重用） （请确保在其中使用了nn.LogSparse和nn.NLLLoss()函数） 将CrossEntropyLoss改为myCELoss类 （不要忘记在类的实例化语法中使用了module.sub()函数来实现子类化） 将CrossEntropyLoss返
    def __init__(self): # 这里只定义了一个参数，其中是一个维度为10的向量
        super().__init__()
    def forward(self,pred,target):
        logprobs = F.log_softmax(pred, dim=1) # log_probs is a tensor of shape (batch_size, num_classes)
        
        target = F.one_hot(target, num_classes=pred.size(1)) # target is a tensor of shape (batch_size, num_
        
        return -torch.sum(target * logprobs,dim=1).mean() # the + is there to make sure the sum is not over
pred = torch.tensor([[0.1,0.9],[0.2,0.8]])
target = torch.tensor([1,0]) # the target is a 1-D tensor with length equal to the number of classes.
print(celoss(pred,target))
myceloss = myCELoss() # myCELoss() is an object of myCELoss class, it can now be called like a function.
print(myceloss(pred,target))