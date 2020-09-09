x=int(input("x değeri için 0 ile 100 arasında bir rakam yazabilir misiniz?"))

if x>0 and x<=19:
  print("ses çok kısık")
elif x>=20 and x<=39:
  print("daha iyi duyabilirim")
elif x>=40 and x<=59:
  print("çok iyi ses")
elif x>=60 and x<=79:
  print("ses gerçekten yükseldi")
elif x>=80 and x>=100:
  print("sesten başım ağrıdı")
