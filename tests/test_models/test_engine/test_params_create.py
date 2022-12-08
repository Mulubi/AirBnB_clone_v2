#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


def test_params_create():
    '''
    test creating an object using,
    a string, float and an int
    '''
    obj1 = do_create("create MyClass param1=value1 param2\
                     =125.125 param3=123")
    assert obj1.param1 == "value1"
    assert obj1.param2 == 125.125
    assert obj1.param3 == 123

    '''
    test creating an object with string params
    that contain " and _
    '''
    obj2 = do_create('create Warren param1="value1"\
                     param2="value_2"')
    assert obj2.param1 == "value1"
    assert obj2.param2 == "value 2"

    '''
    test creating an object with missing
    or invalid params
    '''
    obj3 = do_create("create MyClass")
    assert obj3 is None
    obj4 = do_create("create MyClass param1=value1 param2")
    assert obj4 is None
