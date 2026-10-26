# Core Endian

**Framework**: Core Services  
**Role**: API Collection

Convert data between big endian and little endian format

> **Deprecated**: In macOS 10.8, use the Core Foundation byte order functions described in [Byte-Order Utilities](../../CoreFoundation/byte-order-utilities.md) instead.

## Topics

### Working With Flippers
- [CoreEndianInstallFlipper](../api-1575602-coreendianinstallflipper.md)
  Installs a flipper callback for the specified data type.
- [CoreEndianGetFlipper](../api-1575564-coreendiangetflipper.md)
  Obtains the flipper callback that is installed for thespecified data type.
- [CoreEndianFlipData](../api-1575610-coreendianflipdata.md)
  Calls the flipper callback associated with the specifieddata type.
### Changing the Endian Format
- [Endian16_Swap](../endian16_swap.md)
  Changes the endian format of an unsigned 16-bit integer.
- [Endian32_Swap](../endian32_swap.md)
  Changes the endian format of an unsigned 32-bit integer.
- [Endian64_Swap](../endian64_swap.md)
  Changes the endian format of an unsigned 64-bit integer.
### Converting from Big-Endian to Native Format
- [EndianS16_BtoN](../endians16_bton.md)
  Converts a signed 16-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianS32_BtoN](../endians32_bton.md)
  Converts a signed 32-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianS64_BtoN](../endians64_bton.md)
  Converts a signed 64-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianU16_BtoN](../endianu16_bton.md)
  Converts an unsigned 16-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianU32_BtoN](../endianu32_bton.md)
  Converts an unsigned 32-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianU64_BtoN](../endianu64_bton.md)
  Converts an unsigned 64-bit big-endian value to the equivalentvalue in the computer’s native format.
### Converting from Native Format to Big-Endian Format
- [EndianS16_NtoB](../endians16_ntob.md)
  Converts a signed 16-bit value in the computer’s nativeformat to the equivalent big-endian value.
- [EndianS32_NtoB](../endians32_ntob.md)
  Converts a signed 32-bit value in the computer’s nativeformat to the equivalent big-endian value.
- [EndianS64_NtoB](../endians64_ntob.md)
  Converts a signed 64-bit value in the computer’s nativeformat to the equivalent big-endian value.
- [EndianU16_NtoB](../endianu16_ntob.md)
  Converts an unsigned 16-bit value in the computer’snative format to the equivalent big-endian value.
- [EndianU32_NtoB](../endianu32_ntob.md)
  Converts an unsigned 32-bit value in the computer’snative format to the equivalent big-endian value.
- [EndianU64_NtoB](../endianu64_ntob.md)
  Converts an unsigned 64-bit value in the computer’snative format to the equivalent big-endian value.
### Converting from Little-Endian Format to Native Format
- [EndianS16_LtoN](../endians16_lton.md)
  Converts a signed 16-bit little-endian value to the equivalentvalue in the computer’s native format.
- [EndianS32_LtoN](../endians32_lton.md)
  Converts a signed 32-bit little-endian value to the equivalentvalue in the computer’s native format.
- [EndianS64_LtoN](../endians64_lton.md)
  Converts a signed 64-bit little-endian value to the equivalentvalue in the computer’s native format.
- [EndianU16_LtoN](../endianu16_lton.md)
  Converts an unsigned 16-bit little-endian value to theequivalent value in the computer’s native format.
- [EndianU32_LtoN](../endianu32_lton.md)
  Converts an unsigned 32-bit little-endian value to theequivalent value in the computer’s native format.
- [EndianU64_LtoN](../endianu64_lton.md)
  Converts an unsigned 64-bit little-endian value to theequivalent value in the computer’s native format.
### Converting from Native Format to Little-Endian Format
- [EndianS16_NtoL](../endians16_ntol.md)
  Converts a signed 16-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianS32_NtoL](../endians32_ntol.md)
  Converts a signed 32-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianS64_NtoL](../endians64_ntol.md)
  Converts a signed 64-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianU16_NtoL](../endianu16_ntol.md)
  Converts an unsigned 16-bit value in the computer’snative format to the equivalent little-endian value.
- [EndianU32_NtoL](../endianu32_ntol.md)
  Converts an unsigned 32-bit value in the computer’snative format to the equivalent little-endian value.
- [EndianU64_NtoL](../endianu64_ntol.md)
  Converts an unsigned 64-bit value in the computer’snative format to the equivalent little-endian value.
### Converting from Big-Endian to Little-Endian Format
- [EndianS16_BtoL](../endians16_btol.md)
  Converts a signed 16-bit big-endian value to the equivalentlittle-endian value.
- [EndianS32_BtoL](../endians32_btol.md)
  Converts a signed 32-bit big-endian value to the equivalentlittle-endian value.
- [EndianS64_BtoL](../endians64_btol.md)
  Converts a signed 64-bit big-endian value to the equivalentlittle-endian value.
- [EndianU16_BtoL](../endianu16_btol.md)
  Converts an unsigned 16-bit big-endian value to the equivalentlittle-endian value.
- [EndianU32_BtoL](../endianu32_btol.md)
  Converts an unsigned 32-bit big-endian value to the equivalentlittle-endian value.
- [EndianU64_BtoL](../endianu64_btol.md)
  Converts an unsigned 64-bit big-endian value to the equivalentlittle-endian value.
### Converting From Little-Endian to Big-Endian Format
- [EndianS16_LtoB](../endians16_ltob.md)
  Converts a signed 16-bit little-endian value to the equivalentbig-endian value.
- [EndianS32_LtoB](../endians32_ltob.md)
  Converts a signed 32-bit little-endian value to the equivalentbig-endian value.
- [EndianS64_LtoB](../endians64_ltob.md)
  Converts a signed 64-bit little-endian value to the equivalentbig-endian value.
- [EndianU16_LtoB](../endianu16_ltob.md)
  Converts an unsigned 16-bit little-endian value to theequivalent big-endian value.
- [EndianU32_LtoB](../endianu32_ltob.md)
  Converts an unsigned 32-bit little-endian value to theequivalent big-endian value.
- [EndianU64_LtoB](../endianu64_ltob.md)
  Converts an unsigned 64-bit little-endian value to theequivalent big-endian value.
### Callbacks
- [CoreEndianFlipProc](../coreendianflipproc.md)
  Defines a pointer to a callback function thatbyte-swaps your custom data.
### Data Types
- [BigEndianLong](../bigendianlong.md)
  Protects a big-endian long value from being changed bylittle-endian code.
- [BigEndianUnsignedLong](../bigendianunsignedlong.md)
  Protects a big-endian unsigned long value from being changedby little-endian code.
- [BigEndianShort](../bigendianshort.md)
  Protects a big-endian short value from being changed bylittle-endian code.
- [BigEndianUnsignedShort](../bigendianunsignedshort.md)
  Protects a big-endian unsigned short value from beingchanged by little-endian code.
- [BigEndianFixed](../bigendianfixed.md)
  Protects a big-endian Fixed value from being changed bylittle-endian code.
- [BigEndianUnsignedFixed](../bigendianunsignedfixed.md)
  Protects a big-endian unsigned Fixed value from beingchanged by little-endian code.
- [BigEndianOSType](./core_endian/bigendianostype.md)
  Protects a big-endian OSType value from being changedby little-endian code.
### Constants
- [Domain Types](../api-1575588-domain_types.md)
  Specify the domain to which a flipper callback shouldbe applied.

## See Also

### Other Reference
- [Carbon Core Structures](./carbon_core_structures.md)
- [Carbon Core Enumerations](./carbon_core_enumerations.md)
- [Carbon Core Functions](./carbon_core_functions.md)
- [Carbon Core Data Types](./carbon_core_data_types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/core_endian)*