@given(u'the second number is inputted')
def second_number(context):
    print('The second number is now inputted')

@when(u'the equals button is pressed')
def equals_sign_pressed(context):
    print('The equals button is pressed')


@then(u'we should see the correct result')
def display_result(context):
    print('Correct result')
