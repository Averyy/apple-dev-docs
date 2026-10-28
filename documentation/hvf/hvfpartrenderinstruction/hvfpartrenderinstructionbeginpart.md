# HVFPartRenderInstructionBeginPart

**Framework**: hvf  
**Kind**: case  
**Role**: Enumeration Case

Instruction noting that the scaler is beginning to render the specified part.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
HVFPartRenderInstructionBeginPart
```

## Discussion

The part may be a glyph or part of a glyph. The callback can return `HVFPartRenderActionSkip` only in response to this instruction.

The `HVFPartRenderParams` union will contain the data for `beginPart`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvfpartrenderinstruction/hvfpartrenderinstructionbeginpart)*