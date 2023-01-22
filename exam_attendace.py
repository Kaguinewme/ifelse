class_held=int(input("enter the class_held"))
class_attended=int(input("enter the class_attended"))
percentage=(class_attended/class_held)*100
if percentage<75:
    print("exam not allowed")
else:
    print("exam allowed")