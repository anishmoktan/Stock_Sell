port= {
  'AAPL': {
            "2020-11-16":[2,150],
            "2020-11-17":[7,160],
            "2020-11-18":[4,170],
            "2020-11-19":[10,200],
            "2020-11-20":[5,200]
          },
  'TSLA': {
            "2020-11-16":[5,150],
            "2020-11-17":[2,160]
          },
  'HOME':
          {
            "2020-11-16":[8,150],
            "2020-11-17":[2,160]
          }
  }


print("\n\n\n")
print("Calling update port function:")
updated_port={}

def update_port(portfolio,updated,date_today):
  for stock in portfolio:
    access = portfolio[stock]
    quant=0

    for date in access:
      quant= quant + access[date][0]
    
      updated[stock]= {date_today:[quant]}

    #   updated[stock]={date_today:x}

update_port(port,updated_port,"Nov20")

print("updated port:")
print(updated_port)


print("End of update port")
print("\n\n\n")
    

    







#delete 5

#DOLMA
# def sell_stock(stock_name,quantity):
#   stock = port[stock_name]
#   for dates in stock:
#     # count=0
#     if stock[dates][0] < quantity:
#       quantity=quantity-int(dates[0])
#       # del stock[dates]
#       stock[dates].clear()
#       #stock.pop(dates,None)
#       # count = count + 1

#     elif stock[dates][0] > quantity:
#       val=str(int(dates[0])-quantity)
#       stock={dates:val}
    
#     elif stock[dates][0] == quantity:
#       stock[dates].clear()
#       # count =count+1
    
#   # if count>0:
  

#ANISH
def sell(stock_name,quantity):
    quant=quantity
    stock=port[stock_name]
    print("Apple stocks in portfolio before deleting " + str(quant)+ " stocks")
    print(stock)

    date_list=[]
    for dates_1 in stock:
        date_list.append(dates_1)

    for dates in date_list: #[nov16, nov17, nov18]
      if stock[dates][0] < quant: # if ['AAPL'][Nov16][0] (2 < 5)
          print("high")
          quant = quant - stock[dates][0]
          stock.pop(dates,None)
          print(quant)
          #print(quantity)
          #print(stock)
          
      elif stock[dates][0] == quant:
          print("Same")
          print(quant)
          stock.pop(dates,None)
          quant = 0

      elif stock[dates][0] > quant:
          print("low")
          print(quant)
          stock[dates][0]= stock[dates][0]-quant
          quant=0

#2,7,4,10
sell('AAPL',10)
print('\n \n \n\n')
print("Apple stocks in portfolio after deleting:") 
print(port["AAPL"])

print('\n \n \n\n')


port['AAPL']['today'] = [1,2]

port['GOOG']= {'jh': [1,2000]}

print(port)

print('\n \n \n\n')

port['GOOG']['today'] = [1,278]
print(port)

print('\n \n \n\n')







  
 
# sell_stock('AAPL',3)
# print(port)

# #!/usr/bin/python
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name']; # remove entry with key 'Name'
# dict.clear(); # remove all entries in dict
# del dict ; # delete entire dictionary
# print "dict['Age']: ", dict['Age']
# print "dict['School']: ", dict['School']
    
# def sell(stock_name,quant):
#     stock=port[stock_name]
#     print(stock)
#     for dates in stock:
#         print(type(stock[dates][0]))













# 'AAPL': {
#             "2020-11-16":[8,150],
#             "2020-11-17":[2,160]
#           },


# Scanario 1
# "On 11-18-2020 sell five stocks for $200" LIFO

# new Portfolio 

# port= {
#   'TSLA': {
#             "2020-11-17":[2,150],
#             "2020-11-16":[3,160]
#           },
#   'HOME':
#           {
#             "2020-11-17":[2,150],
#             "2020-11-16":[3,160]
#           }
#   }

# 'AAPL': {
#             "2020-11-17":[2,150],
#             "2020-11-16":[3,160]
#           },

# ###""""


stocks_list = []
for stocks in port:
  stocks_list.append(stocks)
print(stocks_list)



def total_stocks(name):
  access = port[name]
  total_stocks=0
  for i in access:
    total_stocks=total_stocks+access[i][0]
  print("There are " + str(total_stocks) + " stocks of " + name)

total_stocks('AAPL')

def description(stock_name):
  access = port[stock_name]
  for date, pnq in access.items():
    print("Bought " + str(pnq[0]) + " shares of " + stock_name + " at " + str(pnq[1]) + " on " + str(date))

description('AAPL')

# def sell_stocks(amount,stock_name):
#   while amount < total_stocks(stock_name):
#     access = port[stock_name]
#     for i in access:




# access=port['AAPL']

# networth=0
# for i in access:
#   networth= networth + access[i][0]*access[i][1]

# print(networth)


# sum=0
# for i in access:
#   sum= sum+ access[i][0]

# print (sum)


 
