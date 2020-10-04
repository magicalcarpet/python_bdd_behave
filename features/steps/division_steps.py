@given(u'the numerator is inputted')
def step_impl(context):
    print('The numerator is inputted')


@given(u'the division button is pressed')
def step_impl(context):
    print('The divide button is pressed')


@given(u'the denominator is inputted')
def step_impl(context):
    print('The denomiator is inputted')


@given(u'the equals sign is pressed')
def step_impl(context):
    print('The equal sign is pressed')


@then(u'the dividend is displayed')
def step_impl(context):
    print('The dividend is displayed')
