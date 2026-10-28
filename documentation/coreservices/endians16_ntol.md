# EndianS16_NtoL

**Framework**: Core Services  
**Kind**: macro  
**Role**: Macro

Converts a signed 16-bit value in the computer’s nativeformat to the equivalent little-endian value.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
#define EndianS16_NtoL(value)
```

## Return Value

The equivalent little-endianvalue.

## Parameters

- `value`: A signed 16-bit value in the computer’s native format.

## See Also

### Converting from Native Format to Little-Endian Format
- [EndianS32_NtoL](./endians32_ntol.md)
  Converts a signed 32-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianS64_NtoL](./endians64_ntol.md)
  Converts a signed 64-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianU16_NtoL](./endianu16_ntol.md)
  Converts an unsigned 16-bit value in the computer’snative format to the equivalent little-endian value.
- [EndianU32_NtoL](./endianu32_ntol.md)
  Converts an unsigned 32-bit value in the computer’snative format to the equivalent little-endian value.
- [EndianU64_NtoL](./endianu64_ntol.md)
  Converts an unsigned 64-bit value in the computer’snative format to the equivalent little-endian value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/endians16_ntol)*