import pandas as pd

def main(N, m, t):
    f = open("log.txt", "r")
    cols = ["address", "flag", "first_date", "first_result", "count", "last_date", "last_result", "ave_result", "sub_net"]
    df = pd.DataFrame(index=[], columns=cols)
    pd.set_option('display.max_columns', 9)

    while True:
        broken = df[df["count"]>=N].index.tolist()
        #if broken:
            #print(broken)
        app = []
        for i in range(len(broken)):
            sub_net = broken[i].split(".")[0:3]
            sub_net = ".".join(sub_net)
            app.append(sub_net)
            #print(app)
        len(df[df["count"]>=N])
        if len(app) != len(set(app)):
            print("【警告】故障しているサブネットが検出されました！")
            for i in range(len(broken)):
                if app.count(df.at[broken[i], "sub_net"])>1:
                    print("故障しているサブネット:{}".format(df.at[broken[i], "sub_net"]))
                    print("- 故障状態のサーバアドレス：{}".format(broken[i]))
                    print("- 故障期間：{} から {}".format(str2date(df.at[broken[i], "first_date"]), str2date(date)))
            print("------------------------------------------------------")

        line = f.readline()
        if line:
            date, address, result = line.split(",")
            sub_net = address.split(".")[0:3]
            sub_net = ".".join(sub_net)
            if address not in df["address"]:
                df = df.append(pd.DataFrame({"address":address, "flag":False, "first_date":date, "first_result":result.replace('\n', ''), "count":0, "last_date":None, "last_result":None, "ave_result":result ,"sub_net":sub_net}, index=[address]))
                if "-" in result and df.at[address, "count"]==0:
                    df.at[address, "count"] += 1
                    df.at[address, "flag"] = True
                    #print("add -> {}, count -> {}".format(address, df.at[address, "count"]))
            else:
                df.at[address, "first_result"] = df.at[address, "first_result"]+","+result.replace('\n', '')
                box = []
                box = df.at[address, "first_result"].split(",")
                if (len(box[-1*m:])>=m):
                    sum = 0
                    for i in range(m):
                        if box[-1*i+(-1)] != "-" :
                            sum = sum + int(box[-1*i+(-1)])
                        ave = sum/m
                    #print("ave -> " + str(ave))
                    if ave >= t:
                        print("【警告】負荷状態のサーバがあります！")
                        print("故障状態のサーバアドレス：{}".format(address))
                        #print(box[-1*m:])
                        print("直近{}回における平均応答時間：{}ミリ秒".format(m, ave))
                        print("故障期間：{} から {}".format(str2date(df.at[address, "first_date"]), str2date(date)))
                        print("------------------------------------------------------")
                if "-" in result:
                    df.at[address, "count"] += 1
                    if df.at[address, "flag"] == False:
                        df.at[address, "flag"] = True
                        df.at[address, "first_date"] = date
                        df.at[address, "first_result"] = result.replace('\n', '')
                        ##print("address -> {}, Fdate -> {}, count -> {}".format(address, df.at[address, "first_date"], df.at[address, "count"]))
                    if df.at[address, "count"]>=N:
                        print("故障状態のサーバアドレス：{}".format(address))
                        print("故障期間：{} から {}".format(str2date(df.at[address, "first_date"]), str2date(date)))
                        print("------------------------------------------------------")
                    else:
                        pass
                else:
                    if df.at[address, "count"]>=N:
                        print("故障状態のサーバアドレス：{}".format(address))
                        print("故障期間：{} から {}".format(str2date(df.at[address, "first_date"]), str2date(date)))
                        print("------------------------------------------------------")
                    df.at[address, "flag"] = False
                    df.at[address, "count"] = 0

        else:
            #print("break")
            break
    f.close() 
    #print(df)

def str2date(date):
    YYYY = date[0:4]
    MM = date[4:6]
    DD = date[6:8]
    hh = date[8:10]
    mm = date[10:12]
    ss = date[12:14]
    DATE = str(YYYY +  "年" + MM + "月" + DD + "日" + hh + "時" + mm + "分" + ss + "秒")
    return DATE

if __name__ == "__main__":
    N = 2
    m = 2
    t = 10
    main(N, m, t)