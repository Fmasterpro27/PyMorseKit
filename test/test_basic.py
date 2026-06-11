from pymorsekit import encode, decode


def test_encode_sos():
    assert encode("SOS") == "... --- ..."


def test_decode_sos():
    assert decode("... --- ...") == "SOS"


def test_encode_hello():
    assert encode("HELLO") == ".... . .-.. .-.. ---"


def test_decode_hello():
    assert decode(".... . .-.. .-.. ---") == "HELLO"