# https://www.youtube.com/watch?v=bD05uGo_sVI


import random
import time

names = ['John', 'Fero', 'Imro', 'Stefan', 'Rick', 'Tom']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.time()
people = people_generator(1000000)
t2 = time.time()
duration = t2 - t1


print('took ' + str(duration) + ' seconds')