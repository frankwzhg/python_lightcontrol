import pandas as pd

data_list = ['111', '120', '11221', '208', '214', '10181', '111', '120', '11221', '208', '214', '10180', '10179', '111', '120', '11221']
data_dict_Main_LSwitch_list = []
data_dict_Main_LSwitch = {}
data_dict_Bath_LSwitch_list = []
data_dict_Bath_LSwitch = {}
data_dict_test1_LSwitch_list = []
data_dict_test1_LSwitch = {}
data_dict_test2_LSwitch_list = []
data_dict_test2_LSwitch = {}
data_dict_Bath_LightSensor_list = []
data_dict_Bath_LightSensor = {}
data_dict_Main_LightSensor_list = []
data_dict_Main_LightSensor = {}
for i in range(len(data_list)):
    if data_list[i][0:2] == "11" and len(data_list[i])==3:
        data_dict_Main_LSwitch_list.append(data_list[i][-1:len(data_list[i])])
        data_dict_Main_LSwitch = {"Main_LSwitch":data_dict_Main_LSwitch_list}
    if data_list[i][0:2] == "11" and len(data_list[i])>3:
        data_dict_Main_LightSensor_list.append(data_list[i][-3:len(data_list[i])])
        data_dict_Main_LightSensor = {"Main_LightSensor":data_dict_Main_LightSensor_list}
    # if data_list[i][0:2] == "12" and len(data_list[i])== 3:
    #     data_dict = {"Batch_LSwitch":''.join(data_list[i][-1:len(data_list[i])])}
    #     data_dict_list.append(data_dict)
    # if data_list[i][0:2] == "20" and len(data_list[i])== 3:
    #     data_dict = {"test1":''.join(data_list[i][-1:len(data_list[i])])}
    #     data_dict_list.append(data_dict)
    # if data_list[i][0:2] == "21" and len(data_list[i])== 3:
    #     data_dict = {"test2":''.join(data_list[i][-1:len(data_list[i])])}
    #     data_dict_list.append(data_dict)
    # if data_list[i][0:2] == "10" and len(data_list[i])> 3:
    #     data_dict = {"test2":''.join(data_list[i][-3:len(data_list[i])])}
    #     data_dict_list.append(data_dict)
    # if data_list[i][0:2] == "11" and len(data_list[i])>=3:
    #     data_list[i] = {"Main_LightSensor":''.join(data_list[2:len(data_list[i])])}

Main_LSwitch_Datafram = pd.DataFrame(data_dict_Main_LSwitch)
print Main_LSwitch_Datafram
Main_LightSensor_Datafram = pd.DataFrame(data_dict_Main_LightSensor)
print Main_LightSensor_Datafram
# print data_list
# print data_dict_list
# data_frame = pd.DataFrame(data_dict_list)
# data_frame.


def dataframe_struct(data_list, sensor_type):
    dict_list = []
