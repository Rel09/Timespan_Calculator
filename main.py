#Calculate time difference ( hours/minutes only )

import datetime
if __name__ == '__main__':
    while True:
        my_time_string = input("time: ")
        now = datetime.datetime.now()
        my_datetime = datetime.datetime.strptime(my_time_string, "%H:%M")
        my_datetime = now.replace(hour=my_datetime.time().hour, minute=my_datetime.time().minute)
        bor = now - my_datetime
        bor = str(bor)
        bor = bor.replace(":00", "")
        hours, minutes = bor.split(":")
        minute = (int(hours) * 60) + int(minutes)



        #Ive done this for my job, just modify those to fit your needs
        
        if minute < 15:
            print("Gratuit")
        elif minute <= 60:
            print("5$")
        elif minute <= 120:
            print("8$")
        elif minute <= 180:
            print("11$")
        elif minute <= 239:
            print("14$")
        elif minute >= 240:
            print("17$")

