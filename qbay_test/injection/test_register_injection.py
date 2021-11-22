from qbay.models import *


def test_register_injection_name():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        r = register(line, "test0@test.com", "Long3324!!")
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    message = "============== Succ count: {}/{} =============="
    print(message.format(cnt_succ, cnt_all))


def test_register_injection_email():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        r = register("PP1", line, "test0@test.com")
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    message = "============== Succ count: {}/{} =============="
    print(message.format(cnt_succ, cnt_all))


def test_register_injection_password():
    f = open("qbay_test/injection/injection_payload.txt", "r")
    line = f.readline()
    cnt_succ = 0
    cnt_all = 0
    while line:
        print("Testing content: {}".format(line))
        r = register("PP1", "test0@test.com", line)
        if r:
            cnt_succ += 1
        cnt_all += 1
        line = f.readline()
    message = "============== Succ count: {}/{} =============="
    print(message.format(cnt_succ, cnt_all))
