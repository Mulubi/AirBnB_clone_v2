#!/usr/bin/python3
'''
This class tests whether a state has been entered and
the changes have taken effect in the database by
validating if there was a +1 increase in the
process
'''

import unittest
import MySQLdb


class TestCreateState(unittest.TestCase):
    '''
    This class tests whether a state has been entered and
    the changes have taken effect in the database by
    validating if there was a +1 increase in the
    process.
    '''
    def setUp(self):
        ''' Create a connection to the database '''
        self.cnx = MySQLdb.connect(user='hbnb_test',
                                   password='hbnb_test_pwd',
                                   host='localhost',
                                   db='hbnb_test_db')
        self.cursor = self.cnx.cursor()

    def test_create_state(self):
        '''
        Query the states table and get the number
        of records present.
        '''
        self.cursor.execute('SELECT COUNT(*) FROM states')
        num_records = self.cursor.fetchone()[0]

        ''' Create a new state '''
        self.cursor.execute('INSERT INTO states(name)
                            VALUES("California")')
        self.cnx.commit()

        '''
        Query the states table again
        to get the new number of records.
        '''
        self.cursor.execute('SELECT COUNT(*) FROM states')
        num_record_after = self.cursor.fetchone()[0]

        ''' Verify that the records increased by 1 '''
        self.assertEqual(num_records_after, num_records + 1)

    def tearDown(self):
        ''' Close connection to the db '''
        self.cursor.close()
        self.cnx.close()


if __name__ == '__main__':
    unittest.main()
