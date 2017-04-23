  Feature: do simple maths quickly

    Scenario: Add two numbers
      Given that the Calculator app is loaded
      When you enter '5' as the first number in the calculator
      And you enter '6' as the second number
      And you click the 'times' button
      And you click the equals button
      Then the value displayed is the correct sum for the two numbers entered
