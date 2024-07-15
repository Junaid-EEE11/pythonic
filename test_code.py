### Pytest Module 
### To run test make sure to run pytest in the specified file's directory
import pytest

def add(num1:int, num2:int) -> int:
  return num1+num2

def test_1():
  assert add(2,5)==7

@pytest.fixture
def multi ():
  x=1;y=2;
  return (x**2, y**2)

def test_2(multi):
  val= add(multi[0],multi[1])
  assert val==64
