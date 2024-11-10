from send_email import email
from weather import weather
from read_email import reader
e = email
man = reader
w = weather
e.send(man.read(man, r"/run/media/harddisk/Documents/programming/WeatherReport/email_list.txt"), w.report())