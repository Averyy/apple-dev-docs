# EndianU64_NtoL

**Framework**: Core Services  
**Kind**: macro  
**Role**: Macro

Converts an unsigned 64-bit value in the computer’snative format to the equivalent little-endian value.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
#define EndianU64_NtoL(value)
```

#### Return Value

The equivalent little-endianvalue.

## Parameters

- `value`: An unsigned 64-bit value in the computer’s native format.

## See Also

### Converting from Native Format to Little-Endian Format
- [EndianS16_NtoL](./endians16_ntol.md)
  Converts a signed 16-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianS32_NtoL](./endians32_ntol.md)
  Converts a signed 32-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianS64_NtoL](./endians64_ntol.md)
  Converts a signed 64-bit value in the computer’s nativeformat to the equivalent little-endian value.
- [EndianU16_NtoL](./endianu16_ntol.md)
  Converts an unsigned 16-bit value in the computer’snative format to the equivalent little-endian value.
- [EndianU32_NtoL](./endianu32_ntol.md)
  Converts an unsigned 32-bit value in the computer’snative format to the equivalent little-endian value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/endianu64_ntol)*