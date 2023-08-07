import pandas as pd


#So we first gonna read in then csv
df = pd.DataFrame(pd.read_csv(r"C:\\Users\\ZenzeleMabena\\PycharmProjects\\VolatilityArbitrage\\Single_Stock_Option.csv",sep=","))

#Then we want to get a dataframe that will isolate one contract for us
#We are working with a put
contract_df = df[df['Contract Code'] == "20JUN19 MTN CSH 68.92P"]




#Then we want to calculate some deltas at each run data frame
contract_df['Delta'] = (contract_df['MTM Price'] - contract_df.shift(periods=1)['MTM Price'])/(contract_df['Spot'] - contract_df.shift(periods=1)['Spot'])




#Then we can use them to check the difference between current delta and previous delta
hedgeCount = 0
for index in contract_df.index:

    if (contract_df['Delta'][index] != contract_df.shift(periods=1)['Delta'][index]) :
        #If the difference is greater than 0.1 ,then we need to hedge
        if abs(contract_df['Delta'][index] - contract_df.shift(periods=1)['Delta'][index] ) >= 0.1:
            if contract_df['Delta'][index] > contract_df.shift(periods=1)['Delta'][index]:
                print("We hedge by selling the underlying ,the spot is :",contract_df['Spot'][index], "Delta : ",contract_df['Delta'][index] )

            else:

                print("We hedge by buying the underlying , the spot is : ",contract_df['Spot'][index], "Delta : ", contract_df['Delta'][index])
            hedgeCount = hedgeCount +1
        print("No hedge, Delta is : ",contract_df['Delta'][index])



print("We Hedged for a total number of :",hedgeCount," out of ",len(contract_df.index))




# Essential;ly,if we are going long on volatility then we expect to hedge for a decent amount of time for us to make profit
#And if we are going short on volatility then we dont want to hedge that miuch because that would mean we are losing monwey from the premiums
#paid to us

#All in All : I think we should count the number of hedging instances that occur
#I mean this would actually help us determine whether we took the right position on volatility or not










