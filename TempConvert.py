#TempConvert.py
#Name: Nathan Heavican
#Date: 2-4-26
#Assignment: Lab 3
#Purpose: Create a program that asks the user for a temperature in Fahrenheit, converts it to Celsius, and displays the result clearly.


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Please enter a temperature in Fahrenheit: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = round((tempF-32)*(5/9), 1)
  #Output converted temperature.
  print(tempF, "degrees Fahrenheit is ", tempC, "degrees Celsius.")
if __name__ == '__main__':
  main()
