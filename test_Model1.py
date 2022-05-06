import unittest
import pandas as pd
from Model import Calculations

def testData():
  df = pd.read_excel('./testdata/TestData.xlsx', sheet_name = 'Calculation1')
  thisList = []
  for i in df.index:
    temp = (df['Operand1'][i], df['Operand2'][i], df['Result'][i])
    thisList.append(temp)  
  return thisList

class testClass(unittest.TestCase):

    def test_0(self):
        model = Calculations()
        for row in testData():
            assert model.calculation1(row[0], row[1]) == row[2]