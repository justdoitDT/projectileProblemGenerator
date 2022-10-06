#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:51:19 2021

@author: david.thomas
"""

import math
import random


def run():
    def printAnswers():
        print(
            '\n\n\n\n'
            'From launch until the object lands:\n\n'
            'xi = 0 m              yi = ' + str(hlaunch) + ' m\n'
                                                           'xf = ' + str(
                round(xlaunchland, 1)) + ' m         yf = ' + str(hland) + ' m\n'
                                                                           'Δx = ' + str(
                round(xlaunchland, 1)) + ' m         Δy = ' + str(hland - hlaunch) + ' m\n\n'
                                                                                     'vix = ' + str(
                vxR) + ' m/s       viy = ' + str(vylaunchR) + ' m/s\n'
                                                              'vfx = ' + str(vxR) + ' m/s       vfy = ' + str(
                round(vyland, 1)) + ' m/s\n\n'
                                    '             ti = 0 s\n'
                                    '             tf = ' + str(round(tlaunchland, 1)) + ' s\n'
                                                                                        '             Δt = ' + str(
                round(tlaunchland, 1)) + ' s\n\n\n'
                                         'From launch until the object reaches max height:\n\n'
                                         'xi = 0 m              yi = ' + str(hlaunch) + ' m\n'
                                                                                        'xf = ' + str(
                round(xlaunchhmax, 1)) + ' m         yf = ' + str(round(hmax, 1)) + ' m\n'
                                                                                    'Δx = ' + str(
                round(xlaunchhmax, 1)) + ' m         Δy = ' + str(round(hmax - hlaunch)) + ' m\n\n'
                                                                                           'vix = ' + str(
                vxR) + ' m/s       viy = ' + str(vylaunchR) + ' m/s\n'
                                                              'vfx = ' + str(vxR) + ' m/s       vfy = 0 m/s\n\n'
                                                                                    '             ti = 0 s\n'
                                                                                    '             tf = ' + str(
                round(tlaunchhmax, 1)) + ' s\n'
                                         '             Δt = ' + str(round(tlaunchhmax, 1)) + ' s\n\n\n'
                                                                                             'From the object reaching max height until it lands\n\n'
                                                                                             'xi = ' + str(
                round(xlaunchhmax, 1)) + ' m         yi = ' + str(hmaxR) + ' m\n'
                                                                           'xf = ' + str(
                round(xhmaxland, 1)) + ' m         yf = ' + str(hland) + ' m\n'
                                                                         'Δx = ' + str(
                round(xhmaxland, 1)) + ' m         Δy = ' + str(round(hland - hmax)) + ' m\n\n'
                                                                                       'vix = ' + str(
                vxR) + ' m/s       viy = 0 m/s\n'
                       'vfx = ' + str(vxR) + ' m/s       vfy = ' + str(round(vyland, 1)) + ' m/s\n\n'
                                                                                           '             ti = ' + str(
                round(tlaunchhmax, 1)) + ' s\n'
                                         '             tf = ' + str(round(tlaunchland, 1)) + ' s\n'
                                                                                             '             Δt = ' + str(
                round(tlaunchland - tlaunchhmax, 1)) + ' s\n\n\n\n'
        )

    g = float(input("Enter your approximation for g in m/s^2:  "))
    print('g = ' + str(g) + ' m/s^2\n')
    stopAltogether = False
    correctAnswers = 0
    while stopAltogether == False:
        answersRevealed = False
        hlaunch = random.randint(0, 200)
        thetalaunch = random.randint(15, 89) * 3.14159 / 180
        vlaunch = random.randint(25, 500)
        hmax = (vlaunch * math.sin(thetalaunch)) ** 2 / (2 * g) + hlaunch
        hland = random.randint(0, math.floor(hmax))

        hmaxR = round(hmax, 1)

        vylaunch = vlaunch * math.sin(thetalaunch)
        vylaunchR = round(vylaunch, 1)

        vx = vlaunch * math.cos(thetalaunch)
        vxR = round(vx, 1)

        tlaunchhmax = vylaunch / g
        tlaunchhmaxR = round(vylaunchR / g, 1)

        xlaunchhmax = vx * tlaunchhmax
        xlaunchhmaxR = round(vxR * tlaunchhmax, 1)

        thmaxland = (2 / g * (hmax - hland)) ** .5
        thmaxlandR = round((2 / g * (hmaxR - hland)) ** .5, 1)

        xhmaxland = vx * thmaxland
        xhmaxlandR = round(vxR * thmaxlandR, 1)

        vyland = -(vylaunch ** 2 - 2 * g * (hland - hlaunch)) ** .5
        vylandR = round(-(vylaunchR ** 2 - 2 * g * (hland - hlaunch)) ** .5, 1)
        vylandwrong = -vyland
        vylandRwrong = -vylandR

        tlaunchland = (vylaunch - vyland) / g
        tlaunchlandR = round((vylaunchR - vylandR) / g, 1)
        tlaunchlandwrong = (vylaunch - vylandwrong) / g
        tlaunchlandRwrong = round((vylaunchR - vylandRwrong) / g, 1)

        xlaunchland = vx * tlaunchland
        xlaunchlandR = round(vxR * tlaunchlandR, 1)
        xlaunchlandwrong = vx * tlaunchlandwrong
        xlaunchlandRwrong = round(vxR * tlaunchlandRwrong, 1)

        vland = (vx ** 2 + vyland ** 2) ** .5
        vlandR = round((vxR ** 2 + vylandR ** 2) ** .5, 1)
        vlandwrong = (vx ** 2 + vylandwrong ** 2) ** .5
        vlandRwrong = round((vxR ** 2 + vylandRwrong ** 2) ** .5, 1)

        thetaland = math.degrees(math.atan(vland / vx) + 360)
        thetalandR = round(math.degrees(math.atan(vlandR / vxR) + 360), 1)
        thetalandwrong = math.degrees(math.atan(vlandwrong / vx) + 360)
        thetalandRwrong = round(math.degrees(math.atan(vlandRwrong / vxR) + 360), 1)

        print(
            '\nInitial velocity = ' + str(vlaunch) + ' m/s\n'
                                                     'Launch angle = ' + str(round(thetalaunch * 180 / 3.14159)) + '°\n'
                                                                                                                   'Launch height = ' + str(
                hlaunch) + ' m\n'
                           'Landing height = ' + str(hland) + ' m\n')

        quantityMatrix = [
            [0, "object's horizontal displacement between launch and the object reaching max height",
             min(xlaunchhmax, xlaunchhmaxR), max(xlaunchhmax, xlaunchhmaxR), xlaunchhmax, 'm'],
            [1, "object's horizontal position when it is at max height", min(xlaunchhmax, xlaunchhmaxR),
             max(xlaunchhmax, xlaunchhmaxR), xlaunchhmax, 'm'],
            [2, "object's horizontal velocity at launch", min(vx, vxR), max(vx, vxR), vx, 'm/s'],
            [3, "object's horizontal velocity when it is at max height", min(vx, vxR), max(vx, vxR), vx, 'm/s'],
            [4, "object's vertical displacement between launch and the object reaching max height",
             min(hmax, hmaxR) - hlaunch, max(hmax, hmaxR) - hlaunch, hmax - hlaunch, 'm/s'],
            [5, "object's max height", min(hmax, hmaxR), max(hmax, hmaxR), hmax, 'm'],
            [6, "object's vertical velocity at launch", min(vylaunch, vylaunchR), max(vylaunch, vylaunchR), vylaunch,
             'm/s'],
            [7, "object's vertical velocity when it reaches max height", 0, 0, 0, 'm/s'],
            [8, "time at which the object reaches max height", min(tlaunchhmax, tlaunchhmaxR),
             max(tlaunchhmax, tlaunchhmaxR), tlaunchhmax, 's'],
            [9, "object's horizontal displacement between it reaching max height and landing",
             min(xhmaxland, xhmaxlandR), max(xhmaxland, xhmaxlandR), xhmaxland, 'm'],
            [10, "object's horizontal position when it lands", min(xlaunchland, xlaunchlandR),
             max(xlaunchland, xlaunchlandR), xlaunchland, 'm'],
            [11, "object's horizontal velocity as it lands", min(vx, vxR), max(vx, vxR), vx, 'm/s'],
            [12, "object's vertical displacement between it reaching max height and landing", hland - max(hmax, hmaxR),
             hland - min(hmax, hmaxR), hland - hmax, 'm'],
            [13, "object's vertical velocity as it lands", min(vyland, vylandR), max(vyland, vylandR), vyland, 'm/s'],
            [14, "time at which the object lands", min(tlaunchland, tlaunchlandR), max(tlaunchland, tlaunchlandR),
             tlaunchland, 's'],
            [15, "change in time between the object reaching max height and landing", min(thmaxland, thmaxlandR),
             max(thmaxland, thmaxlandR), thmaxland, 's'],
            [16, "object's horizontal displacement between launch and the object landing",
             min(xlaunchland, xlaunchlandR), max(xlaunchland, xlaunchlandR), xlaunchland, 'm'],
            [17, "object's vertical displacement between launch and the object landing", hland - hlaunch,
             hland - hlaunch, hland - hlaunch, 'm'],
        ]

        remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        keepGoing = True

        while keepGoing == True and len(remaining) > 0:
            current = remaining[random.randint(0, len(remaining) - 1)]
            remaining.remove(current)

            while True:
                response = input('Determine the ' + quantityMatrix[current][1] + '.\n'
                                                                                 'Round your answer to the tenths place, or enter "quit".'
                                                                                 '\n\n')
                if str.lower(str.strip(str(response))) == 'quit' or str.lower(str.strip(str(response))) == '"quit"':
                    print('The correct answer was ' + str(round((quantityMatrix[current][4]), 1)) + ' ' + str(
                        quantityMatrix[current][5]) + '.\n')
                    break
                else:
                    try:
                        if '.' in response:
                            extraRoundingText = ''
                        else:
                            extraRoundingText = ' Remember to round to the TENTHS place.'
                        if not (float(response) >= quantityMatrix[current][2] and float(response) <=
                                quantityMatrix[current][3]):
                            print('Incorrect. Please try again.' + extraRoundingText + '\n')
                        else:
                            print(str(round((quantityMatrix[current][4]), 1)) + ' ' + str(
                                quantityMatrix[current][5]) + ' is correct!\n\n')
                            correctAnswers += 1
                            break
                    except:
                        print('Your answer must be numerical. Please try again.\n')

            while True:
                userInput = input('Enter "another" for another problem using the same initial conditions.\n'
                                  'Enter   "new"   to start from scratch with new initial conditions.\n'
                                  'Enter "answers" to reveal the correct values for all quantities.\n'
                                  'Enter   "end"   to stop practicing for now.\n\n')
                if str.lower(str.strip(userInput)) == 'another':
                    break
                elif str.lower(str.strip(userInput)) == 'answers':
                    printAnswers()
                    answersRevealed = True
                    keepGoing = False
                    break
                elif userInput == 'new':
                    keepGoing = False
                    break
                elif userInput == 'end':
                    keepGoing = False
                    stopAltogether = True
                    print('Thanks for practicing Physics! You correctly solved ' + str(
                        correctAnswers) + ' problems. Have a nice day :)')
                    break
                else:
                    print('Invalid input\n')

            if answersRevealed == True:
                while True:
                    userInput = input(
                        'Enter   "new"   to start from scratch with new initial conditions.\n'
                        'Enter   "end"   to stop practicing for now.\n\n')
                    if userInput == 'new' or userInput == 'another':
                        keepGoing = False
                        break
                    elif userInput == 'end':
                        keepGoing = False
                        stopAltogether = True
                        print('Thanks for practicing Physics! You correctly solved ' + str(
                            correctAnswers) + ' problems. Have a nice day :)')
                        break
                    else:
                        print('Invalid input\n')

            if len(remaining) <= 0:
                print('\n' + "That's all of the problems for these initial conditions. Here are those answers again:")
                printAnswers()
                while True:
                    userInput = input('Enter   "new"   to start from scratch with new initial conditions.\n'
                                      'Enter   "end"   to stop practicing for now.\n\n')
                    if userInput == 'new' or userInput == 'another':
                        keepGoing = False
                        break
                    elif userInput == 'end':
                        keepGoing = False
                        stopAltogether = True
                        print('Thanks for practicing Physics! You correctly solved ' + str(
                            correctAnswers) + ' problems. Have a nice day :)')
                        break
                    else:
                        print('Invalid input\n')


run()
