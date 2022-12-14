#!/usr/bin/env python3
import random
from operator import add, mul, sub
TASK = 'What is the result of the expression?'


def generate_round():
    dct = {'+': add, '*': mul, '-': sub}
    rand_operator = random.choices('+-*')
    a = random.randrange(1, 100)
    b = random.randrange(1, 100)
    answer = dct[rand_operator[0]](a, b)
    question = (f'Question: {a} {rand_operator[0]} {b}')
    return question, str(answer)
