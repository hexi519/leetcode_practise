from typing import Dict, List
from util import *
from loguru import logger as log


def inorder(root):
	chs =[1,2,3,4]
	def test_inside(chars):
		chars = chars[2:]
	test_inside(chs)
	print(f"chars after test_inside is {chs}")

	def test_inside2(chars):
		chars = chars.append(3)
	test_inside2(chs)
	print(f"chars after test_inside2 is {chs}")

inorder(skew)