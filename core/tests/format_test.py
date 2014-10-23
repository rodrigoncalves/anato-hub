# -*- coding: utf-8 -*-


class FormatTest():

    def getName(self):
        self.name = str(self.id).split('=')[-1][:-2]
        self.name = self.name.split('test_')[-1]
        self.name = self.name.replace('_', ' ')

    def __str__(self):
        self.getName()
        out = '\r%s %s ' % (self.my_type, self.name.title())
        out = out.ljust(71, '.')
        return out + '\n'
