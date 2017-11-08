income=14000;
yanglaojin=income*0.08;
yiliao=income*0.02;
shiye=income*0.005;
gongji=income*0.07;

incomeafter=income-yanglaojin-yiliao-shiye-gongji
if (incomeafter<3500):
    print (incomeafter)
elif (incomeafter<=5000):
    tax=(incomeafter-3500)*0.03
elif (incomeafter<=8000):
    tax=(5000-3500)*0.03+(incomeafter-5000)*0.1
elif (incomeafter<=12000):
    tax=(5000-3500)*0.3+(8000-5000)*0.1+(incomeafter-8000)*0.2
    
print("税后工资",incomeafter-tax);
print("税：",tax);
print("公积金:",gongji*2)

