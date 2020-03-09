"""If you were on the moon now, your weight will be 16,5% of your earth weight.
To calculate it you have to multiple to 0,165. If next 15 years your weight will
increase 1 kg each year. What will be your weight each year on the moon next
15 years?"""

"""weight = int(input("Enter your weight: "))
resul = weight * 0.165
for weight_in_moon in range(weight,weight + 16):
    resul += 1
    print(resul)
years = 0
while years < 15:
    years += 1 
    print("your weight in moon:  {0}".format(resul),"after each year: ", years)
print(resul, years)"""




"""weight = float(input("Enter"))
resul = weight * 0.165
while resul < weight:
    resul += 1
    print("Hello world", resul)"""


weight = int(input("Enter your weight: "))
resul = weight * 0.165
for weight_in_moon in range(weight,weight + 16):
    resul += 1
    print(f"{weight_in_moon}", resul)
