from datetime import date, datetime, timezone, timedelta
import time
import calendar as calendario

today = date.today()
print(today)

print(datetime.now())

print(today.weekday())
print(calendario.day_name[today.weekday()])

now = datetime.now()
#print(datetime.utcnow()) en 3.12 ya no ejecuta datetime.utcnow()
utc = datetime.now(tz=timezone.utc)

print(now)
print(utc)

fecha1 = date.today()
fecha2 = date(2023,1,1)

print(f"Han transcurrido {(fecha1-fecha2).days} dias desde {fecha2} hasta {fecha1}")

year = 2023
month= 11

print(calendario.month(year,month))

fechaEn20Dias = fecha1 + timedelta(days=50)
print(fechaEn20Dias)



