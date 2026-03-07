"""_summary_
"""

import pytest
from testing_exp.basic_testing import Math


def test_addition0():
    # setup
    input_var1 = 6
    input_var2 = 7
    expected_result = 13
    math_obj = Math()

    # act
    actual_result = math_obj.addition(input_var1, input_var2)

    # assert
    assert actual_result == expected_result


def test_addition1():
    # setup
    input_var1 = "6"
    input_var2 = 7
    math_obj = Math()

    # act, assert
    with pytest.raises(TypeError):
        math_obj.addition(input_var1, input_var2)
