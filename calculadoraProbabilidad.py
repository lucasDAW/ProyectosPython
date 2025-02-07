import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for attribute, value in kwargs.items():
            for v in range(0, value):
                self.contents.append(attribute)

    def draw(self, amount):
        temp = copy.copy(self.contents)
        drawn = []
        if amount > len(temp):
            drawn = temp

        for i in range(0, amount):
            rand = random.choice(temp)
            drawn.append(rand)
            temp.pop(temp.index(rand))
        self.contents = temp
        return drawn

    def __str__(self):
        return f'{self.contents}'


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total = 0
    total_cumple = 0
    original = hat

    for _ in range(num_experiments):
        total += 1
        hat_copy = copy.deepcopy(original)
        bd = hat_copy.draw(num_balls_drawn)
        draw_list = bd

        resultado = []
        for attr, value in expected_balls.items():
            total_valor = 0
            for i in draw_list:

                if attr == i:
                    total_valor += 1

            if total_valor >= value:
                resultado.append(True)

            else:
                resultado.append(False)

        if all(resultado):
            total_cumple += 1

    for _ in range(num_experiments):
        e_hat = copy.deepcopy(hat)

    probability = total_cumple / total
    return probability


testHat = Hat(red=2, blue=1)

hat = Hat(black=6, red=4, green=3)

print(experiment(hat, {'red': 2, 'green': 1}, 5, 2000))

# OTRA FORMA Y MEJOR
import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments


hat = Hat(black=6, red=4, green=3)
print(experiment(hat, {'red': 2, 'green': 1}, 5, 2000))
