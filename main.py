import datetime
if __name__ == '__main__':
    while True:
        my_time_string = input("time: ")
        now = datetime.datetime.now()
        my_datetime = datetime.datetime.strptime(my_time_string, "%H:%M")
        my_datetime = now.replace(hour=my_datetime.time().hour, minute=my_datetime.time().minute)

        # This is not the right method to convert time, but i didnt had access to documentation or whatever so.. :)
        bor = now - my_datetime
        bor = str(bor)
        bor = bor.replace(":00", "")
        hours, minutes = bor.split(":")
        minute = (int(hours) * 60) + int(minutes)

        print(str(minute) + " Minutes Difference")
