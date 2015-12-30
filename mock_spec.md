```
>>> class MyClass:
...     def func(self):
...             return True
... 
>>> 
>>> 
>>> from mock import Mock
>>> myclass_mock = Mock()
>>> 
>>> myclass_mock.i_do_not_exist()
<Mock name='mock.i_do_not_exist()' id='140232820051920'>
>>> 
>>> 
>>> 
>>> # Now with autospec
... my_class_mock = Mock(spec=MyClass)
>>> my_class_mock.i_do_not_exist()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/site-packages/mock.py", line 658, in __getattr__
    raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'i_do_not_exist'
```
