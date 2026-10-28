# EndianU32_LtoN

**Framework**: Core Services  
**Kind**: macro  
**Role**: Macro

Converts an unsigned 32-bit little-endian value to theequivalent value in the computer’s native format.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
#define EndianU32_LtoN(value)
```

## Return Value

The equivalent valuein the computer’s native format.

## Parameters

- `value`: An unsigned 32-bit little-endian value.

## See Also

### Converting from Little-Endian Format to Native Format
- [EndianS16_LtoN](./endians16_lton.md)
  Converts a signed 16-bit little-endian value to the equivalentvalue in the computer’s native format.
- [EndianS32_LtoN](./endians32_lton.md)
  Converts a signed 32-bit little-endian value to the equivalentvalue in the computer’s native format.
- [EndianS64_LtoN](./endians64_lton.md)
  Converts a signed 64-bit little-endian value to the equivalentvalue in the computer’s native format.
- [EndianU16_LtoN](./endianu16_lton.md)
  Converts an unsigned 16-bit little-endian value to theequivalent value in the computer’s native format.
- [EndianU64_LtoN](./endianu64_lton.md)
  Converts an unsigned 64-bit little-endian value to theequivalent value in the computer’s native format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/endianu32_lton)*