miert=str(input("Mire gyűjti Anna a pénzt?"))
nap=int(input("Hány kutyát sétáltat Anna a hétvégén?"))
seta=nap*20
oraperc=seta/60
print("Anna ",oraperc,"dolgozik")
penz=nap*700
if penz>=5000:
    print("Anna egy", miert,"-et szeretne venni és sikerült neki elérnie a célt")
else:print("Anna egy", miert," szeretne venni és nem sikerült neki elérnie a célt")
