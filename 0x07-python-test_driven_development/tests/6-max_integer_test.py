#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

  def test_max_int(self):
    self.assertEqual(max_integer([5, 8, 2, 3]), 8)
    self.assertEqual(max_integer([1]), 1)
    self.assertEqual(max_integer([-2, -5, -18, -1]), -1)
    self.assertEqual(max_integer([-3, 2, 4, 1]), 4)
    self.assertEqual(max_integer([]), None)

  def test_max_str(self):
    self.assertEqual(max_integer(["wtf"]), "wtf")

  def test_max_bol(self):
    self.assertTrue(max_integer([True, False]), True)
