tab=[0,5,6,8,34,67]
elem=6
deb=0
fin=len(tab)-1
trouve = False
while deb<=fin and not trouve:
    m=(deb+fin)//2 
    if tab[m]==elem:
        trouve=True
    else:
        if tab[m]<elem:
            deb=m+1
        else:
            fin=m-1
if trouve:
    print("l'element recherche est",elem)
else:
    print("element introuvable")
 