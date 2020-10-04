@given(u'the first number is inputted')
def first_number(context):
    raise NotImplementedError(u'STEP: Given the first number is inputted')


@given(u'the addition button is pressed')
def button_pressed(context):
    raise NotImplementedError(u'STEP: Given the addition button is pressed')


@given(u'the second number is inputted')
def second_number(context):
    raise NotImplementedError(u'STEP: Given the second number is inputted')


@when(u'the equals button is pressed')
def equals_sign_pressed(context):
    raise NotImplementedError(u'STEP: When the equals button is pressed')


@then(u'we should see the correct result')
def display_result(context):
    raise NotImplementedError(u'STEP: Then we should see the correct result')

