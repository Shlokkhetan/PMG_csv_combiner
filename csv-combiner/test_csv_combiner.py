import unittest
from io import StringIO
import pandas as pd
import csv_combiner
import sys




class test(unittest.TestCase):
    
    test_output = open('test_output.csv', 'w+')


    def test_1(self):
        """checks existennce of file"""
        with self.assertRaises(Exception) as context:
            csv_combiner.combine(['./fixtures/accessories.csv', './fixtures/clothi2ng.csv'])

        self.assertEqual('File does not exist', str(context.exception))

    def test_2(self):
        """checks for file extennsion"""
        with self.assertRaises(Exception) as context:
            csv_combiner.combine(['./fixtures/accessories.csv', './fixtures/clothing.xls'])

        self.assertEqual('File extension is not correct', str(context.exception))

    def test_filename_column_added(self):
        """Checks if the filename collumn is added"""


        output = StringIO()
        sys.stdout = output
        csv_combiner.combine(['./fixtures/accessories.csv', './fixtures/clothing.csv'])
        
        self.test_output.write(output.getvalue())
        self.test_output.close()

    
        self.assertIn('filename', pd.read_csv('test_output.csv',nrows = 1).columns.values)


   
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
