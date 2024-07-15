## some conventions type hints in PEP484, Optional features doesnot create problem at runtime 
## Literal string interpolation PEP498
import typing as t
def multiply ( num1: int, num2:t.Optional[int] = None, *, arguments_required_as_keyword) -> int:
  """Multiplication of two integers"""
  result=None;
  if arguments_required_as_keyword=='sum' and num2 is not None:
    result=num1*num2;
    print(f"the multiplication of two numbers is {result}")
  return result
  
