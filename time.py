import datetime
import sys

today = datetime.datetime.today()
output = open("work_attendance.txt", "a+")
now = datetime.datetime.now()
out = now + datetime.timedelta(hours=8)
output.write(str(print("\r --> In {enter}       \t >> Out {out}\r".format(enter = now, out = out), file=output)))

output.close()