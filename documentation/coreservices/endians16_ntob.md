# EndianS16_NtoB

**Framework**: Core Services  
**Kind**: macro  
**Role**: Macro

Converts a signed 16-bit value in the computer’s nativeformat to the equivalent big-endian value.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
#define EndianS16_NtoB(value)
```

## Return Value

The equivalent big-endianvalue.

## Parameters

- `value`: A signed 16-bit value in the computer’s native format.

## See Also

### Converting from Native Format to Big-Endian Format
- [EndianS32_NtoB](./endians32_ntob.md)
  Converts a signed 32-bit value in the computer’s nativeformat to the equivalent big-endian value.
- [EndianS64_NtoB](./endians64_ntob.md)
  Converts a signed 64-bit value in the computer’s nativeformat to the equivalent big-endian value.
- [EndianU16_NtoB](./endianu16_ntob.md)
  Converts an unsigned 16-bit value in the computer’snative format to the equivalent big-endian value.
- [EndianU32_NtoB](./endianu32_ntob.md)
  Converts an unsigned 32-bit value in the computer’snative format to the equivalent big-endian value.
- [EndianU64_NtoB](./endianu64_ntob.md)
  Converts an unsigned 64-bit value in the computer’snative format to the equivalent big-endian value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/endians16_ntob)*