#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = "states"

    def __init__(self, *args, **kwargs):
        ''' Init method to copy from the BaseModel '''
        super().__init__(*args, **kwargs)
