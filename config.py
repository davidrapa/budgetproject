import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgres://daviddb:cAkLkSNCgT8nyLwVV1Ggd5LFZARkTgJX@dpg-ch9tcd6si8uqs8mo7nh0-a.oregon-postgres.render.com/daviddb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
