import re
import pytest


def check_email_format(email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise Exception('Invalid email format')
        else:
            return "Email format is ok"

def test_email_exception():
    '''
    Se o método chamado não levantar uma exception, o teste falha,
    por isso o resultado dele é ok quando colocamos um email errado
    '''
    with pytest.raises(Exception) as e:
        assert check_email_format("bademail.com")
    assert str(e.value) == 'Invalid email format'

def add_numbers(num1, num2):
    print("Add function started")
    result = num1 + num2
    print("Number added.")
    return result

@pytest.mark.skip(reason="just testing if skip works")
def test_add_numbers():
    result = add_numbers(2,3)
    assert result == 5