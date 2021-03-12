import unittest
from io import StringIO
import pandas as pd
import csv_combiner
import sys




class test(unittest.TestCase):
    
    test_output = open('test_output.csv', 'w+')
    
    # file1 = './fixtures/accessories.csv '
    # file2 = './fixtures/cloth2ing.csv'
    # test_path = 'combined.csv'


    def test_1(self):
        # self.assertRaises(IOError, csv_combiner.combine(['./fixtures_small/accessories.csv', './fixtures_small/clothi2ng.csv']))

        with self.assertRaises(Exception) as context:
            csv_combiner.combine(['./fixtures/accessories.csv', './fixtures/clothi2ng.csv'])

        self.assertEqual('File does not exist', str(context.exception))

    def test_2(self):
        # self.assertRaises(IOError, csv_combiner.combine(['./fixtures_small/accessories.csv', './fixtures_small/clothi2ng.csv']))

        with self.assertRaises(Exception) as context:
            csv_combiner.combine(['./fixtures/accessories.csv', './fixtures/clothing.xls'])

        self.assertEqual('File extension is not correct', str(context.exception))

    def test_filename_column_added(self):


        output = StringIO()
        sys.stdout = output
        csv_combiner.combine(['./fixtures/accessories.csv', './fixtures/clothing.csv'])
        
        # update the test_output.csv file
        self.test_output.write(output.getvalue())
        self.test_output.close()

        # check if the column exists in the produced data-frame
        # with open('test_output.csv') as f:
        df = pd.read_csv('test_output.csv',nrows = 2)
        print(df.columns.values)
        self.assertIn('filename', df.columns.values)


   
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)