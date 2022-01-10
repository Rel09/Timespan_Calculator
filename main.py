import datetime

if __name__ == '__main__':
    while True:
        try:
            time_input = datetime.datetime.strptime(input('specify time in HH:MM format: '), "%H:%M")
            time_now = datetime.datetime.now()

            z = datetime.timedelta(hours=(time_now.hour - time_input.hour), minutes=(time_now.minute - time_input.minute))

            z = z.total_seconds() / 60
            z = int(str(z).replace(".0", ""))

            # z = Total minutes
            if z >= 0:

                if z >= 0 and z <= 14:
                    print(str(z) + ' minutes - Free')

                elif z <= 59:
                    print(str(z) + " minutes - 5$")

                elif z <= 119:
                    print(str(z) + " minutes - 8$")

                elif z <= 179:
                    print(str(z) + " minutes - 11$")

                elif z <= 239:
                    print(str(z) + " minutes - 14$")

                elif z >= 240:
                    print(str(z) + " minutes - 17$")


            else:
                print("Wrong input, please retry [Err 2]")
        except:
            print("Wrong input, please retry [Err 1]")
