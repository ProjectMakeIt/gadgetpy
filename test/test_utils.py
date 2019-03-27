import gadgetpy

def test_valid():
    assert gadgetpy.utils.verifyName('test.usb0')
def test_invalid():
    assert not gadgetpy.utils.verifyName('test')
