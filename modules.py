# Modules

#Import entire greets.py
import greets

greets.sayHello('Robert')

#If you only want to only import one function out of a Module
from greets import sayGoodbye
sayGoodbye('Harold')
