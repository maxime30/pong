from microbit import *
import speech
import random
import radio

paddle_x = 2
paddle_y = 4
paddle_length = 2


ball_x = random.choice([1, 2, 3])
ball_y = 1
ball_length = 1

active = True

time = 500

change_x = random.choice([-1, 1])
change_y = random.choice([-1, 1])

radio.config(group=2)
radio.on()


display.scroll('Hello', wait=False)
speech.say('Hello')

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break

for i in range(paddle_length):
    display.set_pixel(paddle_x + i, paddle_y, 9)

display.set_pixel(ball_x, ball_y, 9)
sleep(time)

while True:
    # process input
    if button_b.was_pressed() and paddle_x < 3:
        paddle_x += 1

    if button_a.was_pressed() and paddle_x > 0:
        paddle_x -= 1

    message = radio.receive()
    if message:
        ball_x, change_x, change_y = [int(number) for number in message.split(',')]
        active = True
        print('{}; {}; {}'.format(ball_x, change_x, change_y))

    # update game
    if ball_x in range(paddle_x, paddle_x + paddle_length) and ball_y == 3:
        change_y *= -1
        time -= 5

    if ball_x == 0 or ball_x == 4:
        change_x *= -1

    if ball_y == 0:
        change_y *= -1
        if active:
            radio.send('{},{},{}'.format(ball_x, change_x, change_y))
            active = False
    # render
    display.clear()

    for i in range(paddle_length):
        display.set_pixel(paddle_x + i, paddle_y, 9)

    if active:
        ball_x += change_x
        ball_y += change_y
        display.set_pixel(ball_x, ball_y, 9)

    sleep(time)

    if ball_y == 4:
        break


# game over
display.clear()
display.show(Image.SAD)
