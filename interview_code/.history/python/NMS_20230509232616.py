#nms https://blog.csdn.net/weixin_38646522/article/details/120180667
import numpy as np
def nms(dets,th):
    x1 = dets[:,0]
    y1 = dets[:,1]
    x2 = dets[:,2]
    y2 = dets[:,3]
    scores = dets[:,4] 
    
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)    
    order = scores.argsort()[::-1] 
    
    keep = []
    for ix in order:
        i = ix     #index of the current bounding box
        xx1 = np.maximum(x1[i],x1[order[1:]])    #current bounding box's left top x point
        yy1 = np.maximum(y1[i],y1[order[1:]])    #current bounding box's left top y point
        xx2 = np.minimum(x2[i],x2[order[1:]])    #current bounding box's right bottom x point
        yy2 = np.minimum(y2[i],y2[order[1:]])    #current bounding box's right bottom y point
        w = np.maximum(0.0, xx2 - xx1 + 1)  #calculate the width of the bounding box
        h = np.maximum(0.0, yy2 - yy1 + 1)  #calculate the height of the bounding box
        inter = w * h     #calculate the intersection of two bounding boxes    #there are 8 bounding box and we can use min(w
        ovr = inter / (areas[i] + areas[order] - inter) #calculate the ovr of the bounding boxes
        inds = np.where(ovr <= th)[0] #select the bounding boxes whose intersection over the union is less than the given threshold

        keep.extend(inds) #add the index of the bounding box to the list of keep bounding boxes
        order = order[inds+1]
    return keep
    