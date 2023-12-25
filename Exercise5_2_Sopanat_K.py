s = int(input("ระยะทาง (หน่วยเป็นกิโลเมตร)"))
t = int(input("เวลา (หน่วยเป็นชั่วโมง)"))
v = s/t
print(v)
if s and t > 1:
  print(v,"Km/hr")
elif s and t < 1:
  print("Error")
