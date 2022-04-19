import pytest
import pandas as pd
from Model import Calculations

def prepareData(operator):
  df = pd.read_excel('./testdata/TestData.xlsx', sheet_name = operator)
  thisList = []
  for i in df.index:
    temp = (df['Operand1'][i], df['Operand2'][i], df['Result'][i])
    thisList.append(temp)  
  return thisList

@pytest.mark.parametrize("operand1, operand2, expectedResult", prepareData('Calculation1'))
def test_1(operand1, operand2, expectedResult):
  model = Calculations()
  assert model.calculation1(operand1, operand2) == expectedResult

@pytest.mark.parametrize("operand1, operand2, expectedResult", prepareData('Calculation2'))
def test_2(operand1, operand2, expectedResult):
  model = Calculations()
  assert model.calculation2(operand1, operand2) == expectedResult



