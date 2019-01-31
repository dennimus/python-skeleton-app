from CoolPackageName import cool_file_name
import pytest


def test_it_should_get_correct_answer_with_two_ints():
    first = 10
    second = 10
    result = 20
    test_result = cool_file_name.add_inputs(first,second)

    assert(test_result == result)


def test_it_should_raise_error_on_first_string_argument():
    first = 'Jamemr joh'
    second = 10
    
    with pytest.raises(TypeError):
        cool_file_name.add_inputs(first,second)

def test_it_should_raise_error_on_second_string_argument():
    first = 10
    second = 'Jamemr joh'
    
    with pytest.raises(TypeError):
        cool_file_name.add_inputs(first,second)

def test_it_should_work_with_negative_input():
    first = -10
    second = 5
    result = -5
    test_result = cool_file_name.add_inputs(first,second)

    assert(test_result == result)


def test_it_should_work_with_zero_as_input():
    first = 0
    second = 5
    result = 5
    test_result = cool_file_name.add_inputs(first,second)

    assert(test_result == result)  


def test_it_should_raise_error_on_empty_argument():
    first = ''
    second = 10
    
    with pytest.raises(TypeError):
        cool_file_name.add_inputs(first,second)
    
def test_it_should_raise_error_on_None_argument():
    first = None
    second = 10
    
    with pytest.raises(TypeError):
        cool_file_name.add_inputs(first,second)


def test_it_should_work_with_maxint_as_input():
    first = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    second = 1
    result = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555556
    test_result = cool_file_name.add_inputs(first,second)

    assert(test_result == result)  