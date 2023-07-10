#ひたすらコマンドとキーを深堀する。
#頭のキーをすべて取得
#コマンドの最初の部分を取り出す
file_paths=[]
for i in range(0,20):
    file_paths.append('sample'+str(i)+'.yml')

import yaml
official_setkey = ["orbs","version","executors","commands","parameters","jobs","workflows"]
def get_command_name(filepath):
    with open(filepath, 'r') as yml:
        config = yaml.safe_load(yml)
    print(f"----------------{filepath}-------------------------")
    get_command_key_or_list(config)
    
def get_command_key_or_list(config):
    for command in config:
        #print(type(config[command]))
        #ここに来たら終了　例　versionとか
        if(type(config[command]) == float):
            print(config[command])
            #print("-------float end---------")
        elif(type(config[command]) == list):
            for i in config[command]:
                #print("top i")
                #print(i)
                if(type(i) == dict):
                    #print("dict")
                    get_command_key_or_list(i)
                elif(type(i) == list):
                    #print("list")
                    for j in i:
                        #print(j)
                        get_command_key_or_list(j)
                else:
                    print("final correct2")
                    print(str(command) + " : " + str(i))
                #print("-------list end---------")
        elif(type(config[command]) == dict):
            #print("---------in dict---------")
            #print(config[command])
            get_command_key_or_list(config[command])
        else:
            print("final correct")
            print(str(command) + " : " + str(config[command]))
    #
for i in file_paths:
    get_command_name(i)
