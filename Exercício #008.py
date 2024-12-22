médida= int(input("Digitema medida em metros: "))
dm= médida * 10
cm= médida * 100
mm= médida * 1000
dam= médida / 10
hm= médida / 100
km= médida / 1000
print("A médida de {}m corresponde: \n {}dm \n {}cm \n {}mm \n {}dam \n {}hm \n {}km".format(médida,dm, cm, mm, dam, hm, km))