import gadgetpy
import os

def test_valid_name():
    assert gadgetpy.utils.verifyName('test.usb0')

def test_invalid_name():
    assert not gadgetpy.utils.verifyName('test')

def test_valid_pointer(fs):
    tmpdir = "/gadgets/"
    fs.create_dir(tmpdir)
    fs.create_file('/sys/class/udc/test')
    assert gadgetpy.utils.verifyPointer(tmpdir,'test')

def test_pointer_in_use(fs):
    tmpdir = "/gadgets/"
    fs.create_dir(tmpdir)
    gadget = gadgetpy.Gadget('testGadget',tmpdir,write=False)
    fs.create_file(os.path.join(tmpdir,'gadget2','UDC'),contents='test.usb0\n')
    fs.create_file('/sys/class/udc/test.usb0')
    assert not gadgetpy.utils.verifyPointer(str(tmpdir),'test.usb0')

def test_invalid_pointer(fs):
    tmpdir = "/gadgets/"
    fs.create_dir(tmpdir)
    fs.create_dir('/sys/class/udc')
    assert not gadgetpy.utils.verifyPointer(tmpdir,'test')
