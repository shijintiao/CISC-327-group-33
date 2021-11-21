from qbay.models import *
from datetime import datetime


def test_create_product_injection_title():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        last_modified_date = datetime.now()
        r = create_product("PP1", line, last_modified_date, "100", "test0@test.com")
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    print("============== Succ count: {}/{} ==============".format(cnt_succ, cnt_all))


def test_create_product_injection_description():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        last_modified_date = datetime.now()
        r = create_product(line, "from brand Alienware and it \
            is brand new", last_modified_date, "100", "test0@test.com")
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    print("============== Succ count: {}/{} ==============".format(cnt_succ, cnt_all))


def test_create_product_injection_price():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        last_modified_date = datetime.now()
        r = create_product("PP1", "from brand Alienware and it \
            is brand new", last_modified_date, line, "test0@test.com")
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    print("============== Succ count: {}/{} ==============".format(cnt_succ, cnt_all))


def test_create_product_injection_owner():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        last_modified_date = datetime.now()
        r = create_product("PP1", "from brand Alienware and it \
            is brand new", last_modified_date, "100", line)
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    print("============== Succ count: {}/{} ==============".format(cnt_succ, cnt_all))
