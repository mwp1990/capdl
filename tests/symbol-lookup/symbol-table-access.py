#!/usr/bin/env python
#
# Copyright 2014, NICTA
#
# This software may be distributed and modified according to the terms of
# the BSD 2-Clause license. Note that NO WARRANTY is provided.
# See "LICENSE_BSD2.txt" for details.
#
# @TAG(NICTA_BSD)
#

from capdl import ELF

elf = ELF('unstripped.bin')
assert elf.get_arch() == 'x86'

# Confirm that the address concurs with the one we get from objdump.
assert elf.get_symbol_vaddr('_start') == 0x08048d48

elf = ELF('stripped.bin')
assert elf.get_arch() == 'x86'

# We shouldn't be able to get the symbol from the stripped binary.
try:
    vaddr = elf.get_symbol_vaddr('_start')
    assert not ('Symbol lookup on a stripped binary returned _start == 0x%0.8x' % vaddr)
except:
    # Expected
    pass
