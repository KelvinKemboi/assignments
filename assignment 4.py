print("Kelvo's Grade as per the marks")

maths=80
english=80
physics=80
history=80
geo=80

mean=(maths+english+physics+history+geo)/5


if mean>=85:
    print("Scored A PLAIN ")

elif 85>=mean>=80:
    print("Got A MINUS")

elif 80>=mean>=70:
    print("Got B PLUS")

elif 70>=mean>=60:
    print("Got B MINUS")

elif 60>=mean>=50:
    print("Got C PLUS")

elif 50>=mean>=40:
    print("Got C MINUS ")

elif 40>=mean>=30:
    print("Scored D PLUS ")

else:
    print("Scored E")

math inpz