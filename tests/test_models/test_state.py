#!/usr/bin/python3
""" File contains the class to test the state functions """

import unittest
import mysql.connector
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """
    @unittest.skipIf(DB_TYPE != 'mysql', 'Test only\
                     applicable for MySQL')
    def setUp(self):
        """ Connect to the test database """
        self.conn = mysql.connector.connect(
                    host='localhost',
                    user='hbnb_test',
                    password='hbnb_test_pwd',
                    db='hbnb_test_db')
        
        """ Create a anew cursor """
        self.cursor = self.conn.cursor()

        """ get the initial number of states in table """
        self.cursor.execute("SELECT COUNT(*) FROM states")
        self.initial_num_records = self.cursor.fetchone()[0]

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_create_state(self):
        """ tests if a new state was truelly created """
        cursor = self.conn.cursor()

        """ Create a new state called California """
        cursor.execute("CREATE STATE name='California'")

        """ verify that the state was added to the db """
        cursor.execute("SELECT * FROM states WHERE\
                       name='California'")
        state = cursor.fetchone()
        self.assertEqual(state['name'], 'California')
        
        """ Get the updated number of states """
        self.cursor.execute("SELECT COUNT(*) FROM states")
        updated_num_records = self.cursor.fetchone()[0]

        """ Verify that the records increased by 1 """
        self.assertEqual(updated_num_records,
                         self.initial_num_records + 1)

    def tearDown(self):
        """ clean up the test database """
        self.cursor.execute("DROP DATABASE hbnb_test_db")
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
