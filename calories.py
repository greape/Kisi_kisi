def calories_burned(duration, exercise):
  if exercise == "berlari":
    return duration * 10
  elif exercise == "bersepeda":
    return duration * 8
  elif exercise == "berenang":
    return duration * 12

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