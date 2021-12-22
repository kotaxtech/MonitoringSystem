import pandas as pd

def str2date(date):
    YYYY = date[0:4]
    MM = date[4:6]
    DD = date[6:8]
    hh = date[8:10]
    mm = date[10:12]
    ss = date[12:14]
    DATE = str(YYYY +  "年" + MM + "月" + DD + "日" + hh + "時" + mm + "分" + ss + "秒")
    return DATE

def main(N ,m, t):
    f = open("log.txt", "r")
    cols = ["address", "flag", "first_date", "first_result", "count", "last_date", "last_result", "ave_result"]
    df = pd.DataFrame(index=[], columns=cols)
    pd.set_option('display.max_columns', 8)

    while True:
        line = f.readline()
        if line:
            date, address, result = line.split(",")
            if address not in df["address"]:
                df = df.append(pd.DataFrame({"address":address, "flag":False, "first_date":date, "first_result":result.replace('\n', ''), "count":0, "last_date":None, "last_result":None}, index=[address]))
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
                    #print("add -> {}, count -> {}".format(address, df.at[address, "count"]))
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


if __name__ == "__main__":
    N = 2
    m = 2
    t = 10
    main(N, m, t)