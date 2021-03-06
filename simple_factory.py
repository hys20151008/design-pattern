# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class ForestFactory:
    def make_sound(self, obj_type):
        return eval(obj_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    ff.make_sound('Cat')
