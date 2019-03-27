import os
import gadgetpy
from pytest import raises

def test_valid_base_path():
    gadget = gadgetpy.Gadget('testGadget','/test/path/',write=False)
    assert gadget.path=='/test/path/testGadget'

def test_fail_on_existing(tmpdir):
    tmpdir.mkdir('testGadget')
    with raises(gadgetpy.GadgetExists):
        testGadget = gadgetpy.Gadget('testGadget',str(tmpdir),write=True)
