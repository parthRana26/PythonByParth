def percent(price, persentage):
    return (price*persentage/100)
    
p=int(input("Enter the Price = "))
pr=int(input("Enter to finding persentage = "))

r = percent(p, pr)

print("Persentage = ",r)
