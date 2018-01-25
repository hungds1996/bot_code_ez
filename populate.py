from mlab import mlab_connect
from bot import Steam_guard_code

from random import choice, randint
from faker import Faker, providers

service_faker = Faker()
mlab_connect()

# Service.drop_collection()
# 
# for _ in range(30):
#     service = Service(name = service_faker.name(),
#                       yob = randint(1997,2000),
#                       gender = randint(0, 1),
#                       height = randint(150, 180),
#                       phone = '0125488512',
#                       occupied = choice([True, False]))
#     service.save()

bot = Steam_guard_code(bot_id = "123",
                       bot_pass = "123",
                       code = ['123','123','123'])

bot.save()
