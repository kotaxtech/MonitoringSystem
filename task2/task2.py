import pandas as pd

def main(N):
    f = open("log.txt", "r")
    cols = ["address", "flag", "first_date", "first_result", "count", "last_date", "last_result"]
    df = pd.DataFrame(index=[], columns=cols)
    pd.set_option('display.max_columns', 7)

    while True:
        line = f.readline()
        if line:
            date, address, result = line.split(",")
            if address not in df["address"]:
                df = df.append(pd.DataFrame({"address":address, "flag":False, "first_date":date, "first_result":result, "count":0, "last_date":None, "last_result":None}, index=[address]))
                if "-" in result and df.at[address, "count"]==0:
                    df.at[address, "count"] += 1
                    df.at[address, "flag"] = True
                    #print("add -> {}, count -> {}".format(address, df.at[address, "count"]))
            else:
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
    main(N)