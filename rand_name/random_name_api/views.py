from random import random, randint

from rest_framework import views, serializers
from rest_framework.response import Response


letter_histogram = (('a', 8.167),
                   ('b', 1.492),
                   ('c', 2.782),
                   ('d', 4.253),
                   ('e', 12.70),
                   ('f', 2.228),
                   ('g', 2.015),
                   ('h', 6.094),
                   ('i', 6.966),
                   ('j', 0.153),
                   ('k', 0.772),
                   ('l', 4.025),
                   ('m', 2.406),
                   ('n', 6.749),
                   ('o', 7.507),
                   ('p', 1.929),
                   ('q', 0.095),
                   ('r', 5.987),
                   ('s', 6.327),
                   ('t', 9.056),
                   ('u', 2.758),
                   ('v', 0.978),
                   ('w', 2.360),
                   ('x', 0.150),
                   ('y', 1.974),
                   ('z', 0.074))


class RandNameGeneratorView(views.APIView):


    def generate_letter(self):
        dist_sum = random() * 100

        for letter_stat in letter_histogram:
            dist_sum -= letter_stat[1]
            if dist_sum < 0:
                return letter_stat[0]


    def generate_name(self, name_length):

        name = ""
        for i in range(name_length):
            name += self.generate_letter()

        return name

    def get_context_data(self):
        context = {}
        context['random_name'] = self.generate_name(randint(4, 10))
        return context


    def get(self, request, *args, **kwargs):
        return Response(self.get_context_data())