from qbay.models import register, login, Create_product
from datetime import date


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None


def test_r4_1_Create_product():
    last_modified_date = date.today()
    product = Create_product("PP1", "from brand Alienware and it \
      is brand new", last_modified_date, 100, "test0@test.com")
    assert product is not None
    # R4-8: A user cannot create products that have the same title.
    product = Create_product("PP1", "from brand Alienware and it is \
      brand new", last_modified_date, 1000, "17hl111@queensu.ca")
    assert product is None
    # R4-1: The title of the product has to be alphanumeric-only, \
    # and space allowed only if it is not as prefix and suffix.
    product = Create_product(" P1", "from brand Alienware and it \
      is brand new", last_modified_date, 100, "test0@test.com")
    assert product is None
    # R4-4: Description has to be longer than the product's title.
    product = Create_product("Pppppppppp2", "from ",
                             last_modified_date, 100, "test0@test.com")
    assert product is None
    # R4-5: Price has to be of range [10, 10000].
    product = Create_product("P2", "from brand Alienware and it \
      is brand new", last_modified_date, 9, "test0@test.com")
    assert product is None
    # R4-7: owner_email cannot be empty. The owner of the \
    # corresponding product must exist in the database.
    product = Create_product("P3", "from brand Alienware and it \
      is brand new", last_modified_date, 100, "")
    assert product is None

    product = Create_product("P4", "from brand Alienware and it \
      is brand new", last_modified_date, 100, "testtest0@test.com")
    assert product is None

    product = Create_product("P5", "from brand Alienware and it \
      is brand new", last_modified_date, 100, "test0@test.com")
    assert product is not None
