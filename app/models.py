from django.db import models
import pymongo
import mongoengine


mongoengine.connect('cazadetesoros', host='mongodb+srv://casaDeTesoros:casaDeTesoros@cluster0-of11h.gcp.mongodb.net/cazadetesoros?retryWrites=true&w=majority')


class User(mongoengine.Document):
    email = mongoengine.StringField()
    name = mongoengine.StringField()
    meta = {'allow_inheritance': True}



class Imdb(mongoengine.EmbeddedDocument):
    id = mongoengine.StringField()
    rating = mongoengine.DecimalField()
    votes = mongoengine.IntField()


class Tomato(mongoengine.EmbeddedDocument):
    meter = mongoengine.IntField()
    image = mongoengine.StringField()
    rating = mongoengine.IntField()
    reviews = mongoengine.IntField()
    fresh = mongoengine.IntField()
    consensus = mongoengine.StringField()
    userMeter = mongoengine.IntField()
    userRating = mongoengine.DecimalField()
    userReviews = mongoengine.IntField()


class Awards(mongoengine.EmbeddedDocument):
    wins = mongoengine.IntField()
    nominations = mongoengine.IntField()
    text = mongoengine.StringField()


class Movie(mongoengine.Document):
    title = mongoengine.StringField()
    year = mongoengine.IntField()
    rated = mongoengine.StringField()
    runtime = mongoengine.IntField()
    countries = mongoengine.ListField()
    genres = mongoengine.ListField()
    director = mongoengine.StringField()
    writers = mongoengine.ListField()
    actors = mongoengine.ListField()
    plot = mongoengine.StringField()
    poster = mongoengine.StringField()
    imdb = mongoengine.EmbeddedDocumentField(Imdb)
    tomato = mongoengine.EmbeddedDocumentField(Tomato)
    metacritic = mongoengine.IntField()
    awards = mongoengine.EmbeddedDocumentField(Awards)
    type = mongoengine.StringField()
    