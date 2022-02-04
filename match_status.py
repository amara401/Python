
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

'''
def http_error(status):
  match status:
    case 400:
	  return "BAD request"
	case 404:
	  return "NOT fount"
	case _:
	  return "Something is wrong with internet"
status = input("Enter the ERROR status:")
http_error(status)
'''
