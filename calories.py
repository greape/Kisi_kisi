def calories_burned(duration, exercise):
  if exercise == "berlari":
    calorie_burn = duration * 10
    print(calorie_burn)
  elif exercise == "bersepeda":
    calorie_burn = duration * 8
    print(calorie_burn)
  elif exercise == "berenang":
    calorie_burn = duration * 12
    print(calorie_burn)
  else: 
    print("Kegiatan tidak ditemukan")

def total_session_burned_cal(*args, each_session_duration):
    a = 0
    for i in args: 
        if i == "berlari": 
            a += (each_session_duration * 10)
        elif i == "bersepeda" :
            a += (each_session_duration*8)
        elif i == "berenang":
            a += (each_session_duration*12)
    print(a)