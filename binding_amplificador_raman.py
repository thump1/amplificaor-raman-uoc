# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_amplificador_raman_amplificador_raman__amplificador_raman(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module amplificador-raman - based on the path /amplificador-raman. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__potencia_bombeo','__longitud_onda_bombeo','__longitud_onda_senal','__ganancia',)

  _yang_name = 'amplificador-raman'
  _yang_namespace = 'urn:amplificador-raman'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__potencia_bombeo = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="potencia-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='potencia', is_config=True)
    self.__longitud_onda_bombeo = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)
    self.__longitud_onda_senal = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-senal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)
    self.__ganancia = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ganancia", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='ganancia', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['amplificador-raman']

  def _get_potencia_bombeo(self):
    """
    Getter method for potencia_bombeo, mapped from YANG variable /amplificador_raman/potencia_bombeo (potencia)

    YANG Description: Potencia de bombeo del amplificador Raman
    """
    return self.__potencia_bombeo
      
  def _set_potencia_bombeo(self, v, load=False):
    """
    Setter method for potencia_bombeo, mapped from YANG variable /amplificador_raman/potencia_bombeo (potencia)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_potencia_bombeo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_potencia_bombeo() directly.

    YANG Description: Potencia de bombeo del amplificador Raman
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="potencia-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='potencia', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """potencia_bombeo must be of a type compatible with potencia""",
          'defined-type': "amplificador-raman:potencia",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="potencia-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='potencia', is_config=True)""",
        })

    self.__potencia_bombeo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_potencia_bombeo(self):
    self.__potencia_bombeo = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="potencia-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='potencia', is_config=True)


  def _get_longitud_onda_bombeo(self):
    """
    Getter method for longitud_onda_bombeo, mapped from YANG variable /amplificador_raman/longitud_onda_bombeo (longitud-onda)

    YANG Description: Longitud de onda de bombeo del amplificador Raman
    """
    return self.__longitud_onda_bombeo
      
  def _set_longitud_onda_bombeo(self, v, load=False):
    """
    Setter method for longitud_onda_bombeo, mapped from YANG variable /amplificador_raman/longitud_onda_bombeo (longitud-onda)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_longitud_onda_bombeo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_longitud_onda_bombeo() directly.

    YANG Description: Longitud de onda de bombeo del amplificador Raman
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """longitud_onda_bombeo must be of a type compatible with longitud-onda""",
          'defined-type': "amplificador-raman:longitud-onda",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)""",
        })

    self.__longitud_onda_bombeo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_longitud_onda_bombeo(self):
    self.__longitud_onda_bombeo = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-bombeo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)


  def _get_longitud_onda_senal(self):
    """
    Getter method for longitud_onda_senal, mapped from YANG variable /amplificador_raman/longitud_onda_senal (longitud-onda)

    YANG Description: Longitud de onda de señal del amplificador Raman
    """
    return self.__longitud_onda_senal
      
  def _set_longitud_onda_senal(self, v, load=False):
    """
    Setter method for longitud_onda_senal, mapped from YANG variable /amplificador_raman/longitud_onda_senal (longitud-onda)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_longitud_onda_senal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_longitud_onda_senal() directly.

    YANG Description: Longitud de onda de señal del amplificador Raman
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-senal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """longitud_onda_senal must be of a type compatible with longitud-onda""",
          'defined-type': "amplificador-raman:longitud-onda",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-senal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)""",
        })

    self.__longitud_onda_senal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_longitud_onda_senal(self):
    self.__longitud_onda_senal = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['1260.00 .. 1675.00']}), is_leaf=True, yang_name="longitud-onda-senal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='longitud-onda', is_config=True)


  def _get_ganancia(self):
    """
    Getter method for ganancia, mapped from YANG variable /amplificador_raman/ganancia (ganancia)

    YANG Description: Ganancia del amplificador Raman
    """
    return self.__ganancia
      
  def _set_ganancia(self, v, load=False):
    """
    Setter method for ganancia, mapped from YANG variable /amplificador_raman/ganancia (ganancia)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ganancia is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ganancia() directly.

    YANG Description: Ganancia del amplificador Raman
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ganancia", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='ganancia', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ganancia must be of a type compatible with ganancia""",
          'defined-type': "amplificador-raman:ganancia",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ganancia", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='ganancia', is_config=True)""",
        })

    self.__ganancia = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ganancia(self):
    self.__ganancia = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ganancia", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='ganancia', is_config=True)

  potencia_bombeo = __builtin__.property(_get_potencia_bombeo, _set_potencia_bombeo)
  longitud_onda_bombeo = __builtin__.property(_get_longitud_onda_bombeo, _set_longitud_onda_bombeo)
  longitud_onda_senal = __builtin__.property(_get_longitud_onda_senal, _set_longitud_onda_senal)
  ganancia = __builtin__.property(_get_ganancia, _set_ganancia)


  _pyangbind_elements = OrderedDict([('potencia_bombeo', potencia_bombeo), ('longitud_onda_bombeo', longitud_onda_bombeo), ('longitud_onda_senal', longitud_onda_senal), ('ganancia', ganancia), ])


class amplificador_raman(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module amplificador-raman - based on the path /amplificador-raman. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Implementa las entidades de un amplificador Raman.
  """
  __slots__ = ('_path_helper', '_extmethods', '__amplificador_raman',)

  _yang_name = 'amplificador-raman'
  _yang_namespace = 'urn:amplificador-raman'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__amplificador_raman = YANGDynClass(base=yc_amplificador_raman_amplificador_raman__amplificador_raman, is_container='container', yang_name="amplificador-raman", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_amplificador_raman(self):
    """
    Getter method for amplificador_raman, mapped from YANG variable /amplificador_raman (container)
    """
    return self.__amplificador_raman
      
  def _set_amplificador_raman(self, v, load=False):
    """
    Setter method for amplificador_raman, mapped from YANG variable /amplificador_raman (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_amplificador_raman is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_amplificador_raman() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_amplificador_raman_amplificador_raman__amplificador_raman, is_container='container', yang_name="amplificador-raman", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """amplificador_raman must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_amplificador_raman_amplificador_raman__amplificador_raman, is_container='container', yang_name="amplificador-raman", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='container', is_config=True)""",
        })

    self.__amplificador_raman = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_amplificador_raman(self):
    self.__amplificador_raman = YANGDynClass(base=yc_amplificador_raman_amplificador_raman__amplificador_raman, is_container='container', yang_name="amplificador-raman", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:amplificador-raman', defining_module='amplificador-raman', yang_type='container', is_config=True)

  amplificador_raman = __builtin__.property(_get_amplificador_raman, _set_amplificador_raman)


  _pyangbind_elements = OrderedDict([('amplificador_raman', amplificador_raman), ])


