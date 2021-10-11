from qbay.models import register, login, Create_product
from datetime import date


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', 'A123456a!') is True
    assert register('u0', 'test1@test.com', 'A123456a!') is True
    assert register('u1', 'test0@test.com', 'A123456a!') is False


def test_r1_1_user_register():
    '''
    Testing R1-1: Both the email and password cannot be empty.
    '''

    assert register('u2', 'test2@test.com', '') is False
    assert register('u3', '', 'A123456a!') is False


def test_r1_3_user_register():
    '''
    Testing R1-3: The email has to follow addr-spec defined in RFC 5322
    '''

    assert register('u4', 'Abc.test.com', 'A123456a!') is False
    assert register('u5', 'a"b(cg<h>i[jk]l@test.com', 'A123456a!') is False
    assert register('u6', 'just"not"right@test.com', 'A123456a!') is False


def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity:
      minimum length 6,
      at least one upper case, at least one lower case,
      and at least one special character.
    '''

    assert register('u7', 'test7@test.com', '123456') is False
    assert register('u8', 'test8@test.com', 'A123456') is False


def test_r1_8_9_10_user_register():
    '''
    Testing R1-8: Shipping address is empty at the time of registration.
    Testing R1-9: Postal code is empty at the time of registration.
    Testing R1-10: Balance should be initialized as 100
      at the time of registration.
    '''

    # u0 login
    user = login('test0@test.com', 'A123456a!')
    assert user.shipping_address == ""
    assert user.postal_code == ""
    assert user.balance == 100


def test_r2_1_user_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', 'A123456a!')
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 'A123457a!')
    assert user is None


def test_r3_2_3_4_update_profile():
    '''
    Testing R3-2: Shipping_address should be non-empty,
      alphanumeric-only, and no special characters such as !.
    Testing R3-3: Postal code has to be a valid Canadian postal code.
    Testing R3-4: User name follows the requirements above.
    '''
    user = login('test0@test.com', 'A123456a!')
    user.updateProfile('u00', '100 Princess St', 'K1L3M9')
    assert user.username == 'u00'
    assert user.shipping_address == '100 Princess St'
    assert user.postal_code == 'K1L3M9'


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
