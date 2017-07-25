#!/usr/bin/python
# -*- coding: utf-8 -*-
# Quiz Game

from string import Template

# Level - Eazy

LEVEL1 = \
    '''
HTML stands for Hyper Text ${blank1} Language.
It describes the ${blank2} of Web pages using markup.
${blank3}' are the building blocks of HTML pages.
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
and '${blank3}. Python is said to be relatively easy to
learn and ${blank4}, meaning its statements can be ${blank5}
in a number of operating systems, including UNIX-based systems,
Mac OS and various versions of Microsoft Windows 98. Python was
created by ${blank6}, a former resident of the ${blank7}, whose
favorite comedy group at the time was Monty Python's Flying Circus.
The ${blank8} code is freely available and open for modification
and reuse. A notable feature of Python is its ${blank9} of source
statements to make the code easier to read. Python offers ${blank10}
data type, ready-made ${blank11}, and ${blank12} to many system
calls and ${blank13}. It can be ${blank14}, using the C or C++ language.
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
${blank6}, ${blank7}, ${blank8}, or any other provider.
Then, industry-standard provisioning tools such as
shell scripts, ${blank9}, or ${blank10}, can automatically
install and configure software on the virtual machine. If
you are a developer, ${blank1} will isolate ${blank17} and
their configuration within a single disposable, consistent
environment, without sacrificing any of the tools you are
used to working with (editors, browsers, debuggers, etc.).
Once you or someone else creates a single ${blank13},
you just need to ${blank14} and everything is ${blank15}
and ${blank16} for you to work. Other members of your team
create their development environments from the same configuration,
so whether you are working on Linux, Mac OS X, or Windows,
all your team members are running code in the same environment,
against the same ${blank17}, all configured the same way.
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
    'blank7': '__7__',
    'blank8': '__8__',
    'blank9': '__9__',
    'blank10': '__10__',
    'blank11': '__11__',
    'blank12': '__12__',
    'blank13': '__13__',
    'blank14': '__14__',
    'blank15': '__15__',
    'blank16': '__16__',
    'blank17': '__17__',
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
    'netherlands',
    'source',
    'indenting',
    'dynamic',
    'class',
    'interfaces',
    'libraries',
    'extended',
    ], [
    'vagrant',
    'reproducible',
    'portable',
    'productivity',
    'flexibility',
    'virtualbox',
    'VMware',
    'AWS',
    'chef',
    'puppet',
    'tools',
    'vagrantfile',
    'vagrant up',
    'installed',
    'configured',
    'dependencies',
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
        print ('Invalid level selection!')
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
    while blank <= len(solution[level - 1]):
        string = Template(levels[level - 1]).substitute(substitution)
        print (string)
        answer = raw_input('\nSubmit Your Answer For'
                           ' blank' + str(blank) + ': ')
        while answer != solution[level - 1][blank - 1]:
            answer = \
                raw_input('\nIncorrect answer! Submit Your Answer For'
                          ' blank' + str(blank) + ': ')
        b = 'blank' + str(blank)
        substitution[b] = answer
        print ('\n Correct.')
        blank += 1
        credit += 1
    if credit == len(solution[level - 1]):
        return 1
    return 0


def main():
    """
        This is the main function that makes an
        initiall function call to start the game.
        It also prints whether the user win or
        loose and also promts for playing again
        or quiting.
    """
    print ('Welcome To The Quiz Game!')
    level = input_level()

    if level <= 3:
        result = start_playing(level)
        if result == 1:
            print ('You Win!')
        else:
            print ('You Loose!')
        play_again = raw_input('Do you want to play again Y/N? : ')
        if play_again == 'Y':
            main()
        else:
            exit()
    else:
        exit()


main()
