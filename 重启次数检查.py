# coding=utf8
import os, re
from xlwt import *

# root_path = raw_input("please input file`s path:")
version = "F1331V0.3.0"
root_path = ".\%s" % version
key = ["QCA4004B version"]
ture_time = ["00:00:00,"]
file_time = ".[2017-10-20_00-00-00].log"

for parents, dirnames, filenames in os.walk(root_path):
    for filename in filenames:
        if "GN" in filename and ".log" not in filename:
            new_name = filename + file_time
            os.renames(os.path.join(parents, filename), os.path.join(parents, new_name))

mac_time = [["1", u"1"],
            ["2", u"2"],
            ["3", u"3"],
            ["4", u"4"],
            ["5", u"5"],
            ["6", u"6"],
            ["7", u"7"],
            ["8", u"8"],
            ["9", u"9"],
            ["10", u"10"],
            ]

mac_index = 1
for i in mac_time:
    i.append(mac_index)
    mac_index += 2

tmp_list = []
mac_dict = {}
for xs, ys, zs in os.walk(root_path):
    for z in zs:
        if "GN" in z:
            mac_tmp = re.findall(r"line-(.+?)-", z)[0][-4:]
            if mac_tmp not in tmp_list:
                mac_dict[mac_tmp] = []
                tmp_list.append(mac_tmp)
                for ii in mac_time:
                    if os.path.join(xs, z).split("\\")[-2] == ii[0]:
                        mac_time[mac_time.index(ii)][0] = mac_tmp
                        break
            file_path = os.path.join(xs, z)
            with open(file_path, "r") as files:
                try:
                    files = files.readlines()
                except:
                    print(files)
                try:
                    for tmp_file in files:
                        for i in key:
                            if i in tmp_file:
                                mac_dict[mac_tmp].append(tmp_file)
                except:
                    print(tmp_file)


total=[]
for k, v in mac_dict.items():
    print (k)
    a=len(v)
    total.append(a)
    print(a)
    for i in v:
        print (i)
print("total time")
sum=0
for i in total:
    sum=sum+i
print(sum)

