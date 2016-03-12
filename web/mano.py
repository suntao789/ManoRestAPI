#coding=utf-8
#author s00279560 20160312
__version__ = '0.1'
import web,sys,re
sys.path.append(sys.path[0] + '/../bin')
from dataprocess import *
#��Ҫ����Դ����
urls = (
    '/v3/auth/tokens','tokens',
    '/v2/vapps/instances/(.*)','vmsprocess'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

class tokens:
    def POST(self):
        web.header("Content-Type","application/json") 
        web.header("X-Subject-Token","7099908ad96c4653acd181fc84214f3c") 
        render = open("templates/tokendata.txt",'r').readlines()
        return ''.join(i.strip("\n") for i in render)
    
class vmsprocess:
    vminfo = []
    singlevminfo = open("templates/vmdata.txt",'r').readlines()
    singlevm = ''.join(i.strip("\n") for i in singlevminfo)
    responsecreatevm = open("templates/createvm.txt",'r').readlines()
    rescreatevm = ''.join(i.strip("\n") for i in responsecreatevm)
    #vm����Ϣ����    
    vm1 = {"name":"OMU1","state":"Active","id":"123456789"}
    vm2 = {"name":"OMU2","state":"Active","id":"987654321"}
    vminfo.append(vm1)
    vminfo.append(vm2)
    def GET(self,data):
        #add header
        web.header("Content-Type","application/json") 
        #process data
        vmdata = AssmbleVMData(self.singlevm,self.vminfo)
        return vmdata
    
    def POST(self,data):
        #process request data
        request_data = web.data()
        inputdata = ''.join(i.strip("\n") for i in request_data)
        #response data
        web.header("Content-Type","application/json")
        #add new vm info to array vminfo         
        vmname,id,response = RepsonseCreateVM(self.rescreatevm,inputdata)
        addvm = {"name":vmname,"id":id}
        self.vminfo.append(addvm)
        return response  
    
    def DELETE(self,data):
        #delete vm info from array vminfo
        m = re.search(r"(\d+)\/vm\/(\d+)",data)
        vnfid,vmid = m.group(1),m.group(2)
        for index,vm in enumerate(self.vminfo):
            if "id" in vm.keys():
                if vm["id"] == vmid:
                    del self.vminfo[index]
        return "OK" 
    
    def PUT(self,data):
        #get the action
        try:
            m = re.search(r"(\d+)\/action",data)
            vmid = m.group(1)
        except AttributeError:
            print "error,the URL is wrong"
            return "error,the URL is wrong"
        #process request data
        request_data = web.data()
        requestdata = ''.join(i.strip("\n") for i in request_data)
        action = VMAction(inputdata = requestdata)
        for index,vm in enumerate(self.vminfo):
            if "id" in vm.keys():
                if vm["id"] == vmid:
                    self.vminfo[index]["state"] =  action     
        return "OK"    

if __name__ == "__main__":
    #print app.request("/v2/vapps/instances/123456789/vm").data
    app.run()