import time
now = 0
was = 0
delta = 0
k = 0
f = open('text.txt', 'w')
now = int(round(time.time() * 1000))
while True:
    if input() == 'stop':
        print("Stoped")
        exit()
        f.close()
    else:
        now = int(round(time.time() * 1000))
        delta = now - was
        was = now
        if k == 0:
            delta = 0
            k = 1
        print(delta)
        f.write('delay(' + str(delta) + ');' + '\n')
        f.write('digitalWrite(relay1pin, 1);' + '\n' + 'delay(10);' + '\n' + 'digitalWrite(relay1pin, 0);' + '\n')
