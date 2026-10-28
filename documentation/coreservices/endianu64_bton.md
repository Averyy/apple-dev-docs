# EndianU64_BtoN

**Framework**: Core Services  
**Kind**: macro  
**Role**: Macro

Converts an unsigned 64-bit big-endian value to the equivalentvalue in the computer’s native format.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
#define EndianU64_BtoN(value)
```

## Return Value

The equivalent valuein the computer’s native format.

## Parameters

- `value`: An unsigned 64-bit big-endian value.

## See Also

### Converting from Big-Endian to Native Format
- [EndianS16_BtoN](./endians16_bton.md)
  Converts a signed 16-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianS32_BtoN](./endians32_bton.md)
  Converts a signed 32-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianS64_BtoN](./endians64_bton.md)
  Converts a signed 64-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianU16_BtoN](./endianu16_bton.md)
  Converts an unsigned 16-bit big-endian value to the equivalentvalue in the computer’s native format.
- [EndianU32_BtoN](./endianu32_bton.md)
  Converts an unsigned 32-bit big-endian value to the equivalentvalue in the computer’s native format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/endianu64_bton)*