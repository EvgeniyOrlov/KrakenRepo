time = int(input('Введите время в секундах'))

hours = time // 3600
minutes = (time - (hours * 3600)) // 60
sec = time % 60

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if sec < 10:
    sec = '0' + str(sec)

print(f'{hours}:{minutes}:{sec}')
