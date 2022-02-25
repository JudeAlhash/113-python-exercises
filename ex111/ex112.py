# EX 112 : Create a new function in the data module, called validateMoney() that validates an input which is
# supposed to be a monetary value.
from utilidadescev import data
from utilidadescev import moeda
a = data.validateMoney('Type the value:')
moeda.doAll(a)