#coding=utf-8
#author s00279560 20160312
__version__ = '0.1'
import json,random
#vminfo��һ�����ݣ������Ԫ�ض����ֵ�
def  AssmbleVMData(singledata,*vminfotuple):
    vms = []
    json_data = json.loads(singledata)
    vminfo = vminfotuple[0]
    for vm in vminfo:
        temp = json_data
        for index in vm.viewkeys():
            temp[index] = vm[index]
        temp = json.dumps(temp)
        vms.append(temp)
    vmsdata = ','.join([i for i in vms])
    return '{"vms":[' + vmsdata + "]}"

def  RepsonseCreateVM(backdata,inputdata):
    input = json.loads(inputdata)
    output = json.loads(backdata)
    output["vms"][0]["vm_name"] = input["vms"][0]["vm_name"]
    output["vms"][0]["id"] = str(int(random.random()*1000000000000))
    return output["vms"][0]["vm_name"],output["vms"][0]["id"],json.dumps(output)
#resst、power on/off、rebuildVM
def  VMAction(inputdata):
    actiondata = ["poweron","poweroff","reset"]
    input = json.loads(inputdata)
    action = input["action"]
    if action == "poweron":
        return "Active"
    elif action == "poweroff":
        return "Stop"
    elif action == "reset":
        return "Active"
    else:
        return "None this action"