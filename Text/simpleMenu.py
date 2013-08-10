#!/usr/bin/env python

def doSomething():
    print'foo'
def doSomethingElse():
    print'bar'

def mainMenu():
	options = ['do something', 'do something else']
	callbacks = [doSomething, doSomethingElse]
	for i,option in enumerate(options):
		print('%s. %s' % (i, option)) # display all options
	choice = int(raw_input('your choice? '))
	callbacks[choice]() # call correspondending function
mainMenu()
