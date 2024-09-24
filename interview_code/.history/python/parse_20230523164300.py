import json
import pdb

def zhushi_lines1(code,doc,skip_lines=10):
    # pdb.set_trace()
    code_split = code.split('\n')
    skip_str = len("".join(code_split[:skip_lines])) + skip_lines
    id = code.find(doc,skip_str)
    st = code[:id].count("\n") 
    print(":id",code[:id]+"@")
    end = st + (doc.count("\n") + 1)
    tail = code[:id].rstrip(" ")[-4:]
    res = [-1,-1]
    
    print("id,st,end",id," ",st," ",end)
    try:
        if  len(tail)==4 and tail[-1] =="\n" and (tail[-4:-1]=='"""' or tail[-4:-1]=="'''"):
            res[0] = st - 1
        else:
            res[0] = st  
            
        # front = code[id+len(doc)+1:].lstrip(" ")[:4]
        front_list = code[id+len(doc):].split("\n")
        if len(front_list) < 2:
            res[1] = end - 1
        else:    
            front = front_list[1]
            if len(front) == 3 and  (front[:3]=='"""' or front[:3]=="'''"):#front[-1] == "\n" and
                res[1] = end
            else:
                res[1] = end - 1
    except Exception as e:
        print(e)
        print(code)
        print(doc)
    
    error = False
    if res == [-1,-1] or res[0]>res[1]:
        # print("error",res)
        error = True
    return res,error
code = '''def send_message(self, data):
        """
          Send websocket data frame to the client.

          If data is a unicode object then the frame is sent as Text.
          If the data is a bytearray object then the frame is sent as Binary.
        """
        opcode = BINARY
        if _check_unicode(data):
            opcode = TEXT

        self._send_message(False, opcode, data)'''
doc = '''Send websocket data frame to the client.

          If data is a unicode object then the frame is sent as Text.
          If the data is a bytearray object then the frame is sent as Binary.'''
res,error = zhushi_lines1(code,doc,skip_lines=0)
print(res)
# fr = open("/share/project/bowen/code_new_data/codesearchnet_train.jsonl","r").readlines()

# for row in fr:
#     # print(row)
#     dic = json.loads(row)
#     if dic["language"] != "python":continue
#     code,doc = dic['func_code_string'],dic['func_documentation_string']
#     res,error = zhushi_lines1(code,doc,skip_lines=0)  
#     print(res)
#     if error:
#         dic_w = {"code":code,"doc":doc}  
#         print(dic_w)  
# print("over")    
    