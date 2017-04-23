from behave import *
from selenium import webdriver


import environment
import time


class Calculator(object):
    @step('that the Calculator app is loaded')
    def app_is_loaded(context):
        context.browser.get(
            'http://seleniumsimplified.com/testpages/calculate.php'
        )

    @step('you enter \'{first_number}\' as the first number in the calculator')
    def enter_first_number(context, first_number):
        first_number_input = context.browser.find_element_by_xpath(
            '//input[@id="number1"]'
        )
        first_number_input.send_keys(first_number)
        context.browser.first_number = int(first_number)

    @step('you enter \'{second_number}\' as the second number')
    def enter_second_number(context, second_number):
        second_number_input = context.browser.find_element_by_xpath(
            '//input[@id="number2"]'
        )
        second_number_input.send_keys(second_number)
        context.browser.second_number = int(second_number)

    @step('you click the \'{operation}\' button')
    def click_option(context, operation):
        option = context.browser.find_element_by_xpath(
            '//option[contains(., "{operation}")]'.format(operation=operation)
        )
        option.click()
        context.browser.option = operation
        #import ipdb; ipdb.set_trace()

    @step('you click the equals button')
    def click_equals(context):
        equals = context.browser.find_element_by_xpath(
            '//input[@id="calculate"]'
        )
        equals.click()

    @step('the value displayed is the correct sum for the two numbers entered')
    def correct_answer(context):
        answer = context.browser.find_element_by_xpath('//span[@id="answer"]')
        answer_text = answer.text
        if context.browser.option == 'plus':
            assert answer_text == str(context.browser.first_number + context.browser.second_number)
        elif context.browser.option == 'minus':
            assert answer_text == str(context.browser.first_number - context.browser.second_number)
        elif context.browser.option == 'times':
            assert answer_text == str(context.browser.first_number * context.browser.second_number)
        elif context.browser.option == 'divide':
            assert answer_text in str(context.browser.first_number / context.browser.second_number)
            #import ipdb; ipdb.set_trace()
