from frozendict import frozendict
from frozen_dict import FrozenDict
from pyrsistent import pmap
from immutables import Map
import copy
import json
import ujson

from data.large_random_dict import LARGE_RANDOM_DICT

SMALL_RANDOM_DICT = {
  'key_one': 'val_one',
  'key_two': 'val_two',
  'key_three': (
    'val_three_a',
    'val_three_b',
    'val_three_c',
    'val_three_d',
  )
}

# from freeze_recursive import freeze


def normal_dict():
  a = {"key_one": ["val_one"]}
  a["key_one"] = ["sweets", "great"]
  return a


def frozen_dict_copy():
  a = frozendict({"key_one": ["val_one"]})
  b = a.copy(key_two=["sweets", "great"])
  # b["key_one"].append('banana')
  # return a
  return a


def frozen_dict_unpack():
  a = frozendict({"key_one": "val_one"})
  b = {**a, **{"key_one": "val_two"}}
  return b["key_one"]


def FrozenDict_unpack():
  a = FrozenDict({"key_one": ("val_one",)})
  b = FrozenDict({**a, **{"key_one": ("sweets", "great")}})
  # return a
  return a


def pyrsistant_pmap():
  a = pmap({"key_one": ("val_one",)})
  b = a + pmap({"key_one": ("sweets", "great")})
  # b = FrozenDict({**a, **{"key_one":("sweets", "great")}})
  # return a
  return b


def Mapit():
  a = Map({"key_one": ("val_one",)})
  b = a.set("key_one", ("sweets", "great"))
  return b


def Mapit_unpack():
  a = Map({"key_one": ("val_one",)})
  b = Map({"key_one": ("sweets", "great")})
  return {**a, **b}


def Mapit_mutate():
  a = Map({"key_one": ("val_one",)})
  b = a.set("key_one", ("sweets", "great"))

  with a.mutate() as mm:
    mm['key_one'] = ("sweets", "great")
    b = mm.finish()

  return b


def run_speed_tests():
  import timeit
  print('normal_dict')
  print(timeit.timeit('''
normal_dict()
''', setup="from __main__ import normal_dict"))

  print('frozen_dict_copy')
  print(timeit.timeit('''
frozen_dict_copy()
''', setup="from __main__ import frozen_dict_copy"))

  print('frozen_dict_unpack')
  print(timeit.timeit('''
frozen_dict_unpack()
''', setup="from __main__ import frozen_dict_unpack"))

  print('FrozenDict_unpack')
  print(timeit.timeit('''
FrozenDict_unpack()
''', setup="from __main__ import FrozenDict_unpack"))

  #     print('pyrsistant_pmap')
  #     print(timeit.timeit('''
  # pyrsistant_pmap()
  # ''', setup="from __main__ import pyrsistant_pmap"))

  print('Mapit')
  print(timeit.timeit('''
Mapit()
''', setup="from __main__ import Mapit"))

  print('Mapit_unpack')
  print(timeit.timeit('''
Mapit_unpack()
''', setup="from __main__ import Mapit_unpack"))

  print('Mapit_mutate')
  print(timeit.timeit('''
Mapit_mutate()
''', setup="from __main__ import Mapit_mutate"))


def normal_dict():
  b = LARGE_RANDOM_DICT
  b['key'] = 'val'
  b['key_two'] = 'val_two'
  b['key_three'] = 'val_three'
  b['key']
  b['key_three']
  b['key']
  return b


def copy_deepcopy():
  a = copy.deepcopy(LARGE_RANDOM_DICT)
  a['key'] = 'val'
  a['key_two'] = 'val_two'
  a['key_three'] = 'val_three'
  a['key']
  a['key_three']
  a['key']
  return a


def json_deepcopy():
  a = json.loads(json.dumps(LARGE_RANDOM_DICT))
  a['key'] = 'val'
  a['key_two'] = 'val_two'
  a['key_three'] = 'val_three'
  a['key']
  a['key_three']
  a['key']
  return a


def ujson_deepcopy():
  a = ujson.loads(ujson.dumps(LARGE_RANDOM_DICT))
  a['key'] = 'val'
  a['key_two'] = 'val_two'
  a['key_three'] = 'val_three'
  a['key']
  a['key_three']
  a['key']
  return a


def immutable_Map(Maparg):
  b = Maparg.set('key', 'val').set('key_two', 'val_two').set('key_three', 'val_three')
  b['key']
  b['key_three']
  b['key']
  return b


if __name__ == '__main__':
  import timeit
  print('normal:       ', end='')
  print(
    timeit.timeit(
      'normal_dict()', setup="import copy; from __main__ import LARGE_RANDOM_DICT, normal_dict", number=100000
    )
  )

  print('deepcopy:       ', end='')
  print(
    timeit.timeit(
      'copy_deepcopy()', setup="import copy; from __main__ import LARGE_RANDOM_DICT, copy_deepcopy", number=1000
    )
  )

  print('json_deepcopy:  ', end='')
  print(
    timeit.timeit(
      'json_deepcopy()', setup="import json; from __main__ import LARGE_RANDOM_DICT, json_deepcopy", number=1000
    )
  )

  print('ujson_deepcopy: ', end='')
  print(
    timeit.timeit(
      'ujson_deepcopy()', setup="import ujson; from __main__ import LARGE_RANDOM_DICT, ujson_deepcopy", number=1000
    )
  )

  print('immutable Map:  ', end='')
  print(
    timeit.timeit(
      'immutable_Map(maparg)',
      setup="from __main__ import LARGE_RANDOM_DICT, immutable_Map; from immutables import Map; maparg = Map(LARGE_RANDOM_DICT)",
      number=100000
    )
  )
