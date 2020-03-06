# 第12章 总结（其一）

class RangeException(Exception):
	"""超范围异常"""
	pass

class ParameterRangeException(RangeException):
	"""超虚参范围异常"""
	pass

class ResultException(RangeException):
	"""超返却值范围异常"""
	pass

def is_valid(value: int) -> bool:
	"""value在0～9之间吗？"""
	return 0 <= value <= 9

def add(a: int, b: int) -> int:
	"""返回a与b的和
	
	前提条件：a和b在0～9之间
			不符合前提条件则抛出ParameterRangeException异常
	
	事后条件：返回的和在0～9之间
			不符合事后条件则抛出ResultRangeException异常
	
	"""
	if not is_valid(a):
		raise ParameterRangeException
	if not is_valid(b):
		raise ParameterRangeException
	
	result = a + b
	
	if not is_valid(result):
		raise ResultException
	return result
		
a = int(input('整数a：'))
b = int(input('整数b：'))

try:
	print('这些数字的和是{}。'.format(add(a, b)))
except RangeException:
	print('范围外。')
except:
	print('产生了某种异常')
finally:
	print('您辛苦了。')