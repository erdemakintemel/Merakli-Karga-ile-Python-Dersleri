ocak=31
şubat=28
mart=31
nisan=30
mayıs=31
haziran=30
temmuz=31
ağustos=31
eylül=30
ekim=31
kasım=30
aralık=31

a=input("hangi aydaki doğalgaz sarfiyatınızı hesaplamak istersiniz? lütfen ay adını hepsi küçük harf olacak şekilde ve tamamen yazınız.")
hangiAy=eval(a)

birimFiyat=1.68

b=input("günlük doğalgaz sarfiyatınızı belirtiniz: ")
günlükSarfiyat=eval(b)

aylikSarfiyat=hangiAy*birimFiyat*günlükSarfiyat

print(aylikSarfiyat)
