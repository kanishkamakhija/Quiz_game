#!/usr/bin/python
# -*- coding: utf-8 -*-

# Quiz Game

from string import Template

# Level - Eazy

LEVEL1 = \
    '''
HTML stands for Hyper Text ${blank1} Language.
It describes the ${blank2} of Web pages using markup.
${blank3} are the building blocks of HTML pages.
HTML elements are represented by ${blank4}.
HTML tags label pieces of content such as "heading",
"paragraph", "table", and so on.
${blank5} do not display the HTML ${blank4},
but use them to render the ${blank6} of the page.
'''

# Level - Medium

LEVEL2 = \
    '''
Python is an ${blank1}, object-oriented programming,
that has gained popularity because of its clear ${blank2}
and ${blank3}. Python is said to be relatively easy to
learn and ${blank4}, meaning its statements can be ${blank5}
in a number of operating systems, including UNIX-based systems,
Mac OS and various versions of Microsoft Windows 98. Python was
created by ${blank6}.
'''

# Level - Hard

LEVEL3 = \
    '''
${blank1} provides easy to configure, ${blank2},
and ${blank3} work environments built on top of
industry-standard technology and controlled by a
single consistent workflow to help maximize the
${blank4} and ${blank5} of you and your team. To
achieve its magic, Vagrant stands on the shoulders
of giants. Machines are provisioned on top of
${blank6}.
'''

levels = [LEVEL1, LEVEL2, LEVEL3]

# substitutes dictionary for our template string

substitution = {
    'blank1': '__1__',
    'blank2': '__2__',
    'blank3': '__3__',
    'blank4': '__4__',
    'blank5': '__5__',
    'blank6': '__6__',
    }

solution = [[
    'markup',
    'structure',
    'elements',
    'tags',
    'browsers',
    'content',
    ], [
    'interpreted',
    'syntax',
    'readability',
    'portable',
    'interpreted',
    'guido van rossum',
    ], [
    'vagrant',
    'reproducible',
    'portable',
    'productivity',
    'flexibility',
    'virtualbox',
    ]]


def input_level():
    """
        This function takes the input from user
        to make a selection of level to play and
        prompts again on invalid input.
    """

    level = input('Enter the level: eazy/medium/hard as 1, 2 or 3 : ')
    if level == 1:
        return 1
    elif level == 2:
        return 2
    elif level == 3:
        return 3
    else:
        print 'Invalid level selection!'
        return input_level()


def start_playing(level):
    """
        This function takes the input as an answer from
        user and progress the quiz by checking the answers
        for each blank. It prompts again fro the answer on
        Incorrect input and return 1 if all answers correct
        or else 0.
    """

    blank = 1
    credit = 0
    wrong = 0
    replace = []
    while blank <= len(solution[level - 1]) + 1:
        if blank == len(solution[level - 1]) + 1:
            break
        answer = raw_input('\nSubmit Your Answer For blank'
                           + str(blank) + ': ')
        while answer != solution[level - 1][blank - 1]:
            answer = \
                raw_input('\nIncorrect answer! Submit Your Answer For blank'
                           + str(blank) + ': ')
            wrong += 1
        b = 'blank' + str(blank)
        replace.append(substitution.get(b))
        substitution[b] = answer
        string = Template(levels[level - 1]).substitute(substitution)
        print string
        print '\n Correct.'
        blank += 1
        credit += 1
    blank = blank - 1
    for i in reversed(replace):
        b = 'blank' + str(blank)
        blank -= 1
        substitution[b] = i
    return credit + wrong


def main():
    """
        This is the main function that makes an
        initiall function call to start the game.
        It also prints whether the user win or
        loose and also promts for playing again
        or quiting.
    """

    print 'Welcome To The Quiz Game!'
    level = input_level()
    if level <= 3:
        string = Template(levels[level - 1]).substitute(substitution)
        print string
        result = start_playing(level)
        print 'Your Score Is : %d' % result
        play_again = raw_input('\n Do you want to play again Y/N? : ')
        if play_again == 'Y':
            main()
        else:
            exit()
    else:
        exit()


main()
