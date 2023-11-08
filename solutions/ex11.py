import datetime

file = open("output.txt","w")
date = datetime.datetime.now()


file.write(f"Todays date is: {date.month}/{date.day}/{date.year}")

file.close()

