import unittest
import sys
import os

from rtler_test_examples import *
from rtler_translate import *

import rtler_debug
debug_verbose = True

class TestSlicesVerilog(unittest.TestCase):


  def setUp(self):
    self.temp_file = self.id().split('.')[-1]
    self.fd = open(self.temp_file, 'w')
    self.compile_cmd = ("iverilog -g2005 -Wall -Wno-sensitivity-entire-vector"
                        "-Wno-sensitivity-entire-array " + self.temp_file)

  def translate(self, model):
    model.elaborate()
    if debug_verbose: rtler_debug.port_walk(model)
    code = ToVerilog(model)
    code.generate( self.fd )
    self.fd.close()

  def test_rotator(self):
    self.translate( Rotator(8) )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_simplesplitter(self):
    self.translate( SimpleSplitter(8) )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_simplemerger(self):
    self.translate( SimpleMerger(8) )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_complexsplitter(self):
    self.translate( ComplexSplitter(16, 4) )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_complexmerger(self):
    self.translate( ComplexMerger(16, 4) )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_wire(self):
    model = Wire(16)
    self.translate( model )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_wire_wrapped(self):
    model = WireWrapped(16)
    self.translate( model )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  def test_register(self):
    model = Register(16)
    self.translate( model )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)
    self.fail( "@posedge_clk translation not implemented yet!" )

  def test_register_wrapped(self):
    model = RegisterWrapper(16)
    self.translate( model )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)
    self.fail( "@posedge_clk translation not implemented yet!" )

  def test_register_chain(self):
    model = RegisterChain(16)
    self.translate( model )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)
    self.fail( "@posedge_clk translation not implemented yet!" )

  def test_register_splitter(self):
    model = RegisterSplitter(16)
    self.translate( model )
    x = os.system( self.compile_cmd )
    self.assertEqual( x, 0)

  #def tearDown(self):
  #  os.remove(self.temp_file)

if __name__ == '__main__':
  unittest.main()