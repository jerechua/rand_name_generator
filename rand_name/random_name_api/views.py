from random import random, randint

from rest_framework import views, serializers
from rest_framework.response import Response

from random_name_generator.views import letter_histogram, conditional_histogram


class RandNameGeneratorView(views.APIView):

    ascii_a = 97

    def generate_letter(self, last_letter):
        dist_sum = random()

        letter_index = ord(last_letter) - self.ascii_a

        index = 0
        for letter_stat in conditional_histogram[letter_index]:
            dist_sum -= letter_stat
            if dist_sum < 0:
                return chr(index + self.ascii_a)
            index += 1


    def generate_name(self, name_length):

        name = ""
        letter = chr(randint(0, 26) + self.ascii_a)

        for i in range(name_length):
            name += letter
            letter = self.generate_letter(letter)

        return name

    def get_context_data(self):
        context = {}
        context['random_name'] = self.generate_name(randint(4, 10))
        return context


    def get(self, request, *args, **kwargs):
        return Response(self.get_context_data())