# PartRenderer.Instruction

**Framework**: hvf  
**Kind**: enum

The set of instructions passed to a render context

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
enum Instruction
```

## Topics

### Enumeration Cases
- [case addCubic(cp1: PartRenderer.Point, cp2: PartRenderer.Point, on: PartRenderer.Point)](partrenderer/instruction/addcubic(cp1:cp2:on:).md)
- [PartRenderer.Instruction.addLine(_:)](partrenderer/instruction/addline(_:).md)
- [PartRenderer.Instruction.addPoint(_:)](partrenderer/instruction/addpoint(_:).md)
- [case addQuad(off: PartRenderer.Point, on: PartRenderer.Point)](partrenderer/instruction/addquad(off:on:).md)
- [PartRenderer.Instruction.beginPart(id:name:)](partrenderer/instruction/beginpart(id:name:).md)
  The name value is for client use and is not set by the loader or scaler
- [PartRenderer.Instruction.beginPath](partrenderer/instruction/beginpath.md)
- [PartRenderer.Instruction.closePath](partrenderer/instruction/closepath.md)
- [PartRenderer.Instruction.endPart(id:name:)](partrenderer/instruction/endpart(id:name:).md)
  The name value is for client use and is not set by the loader or scaler
- [PartRenderer.Instruction.endPath](partrenderer/instruction/endpath.md)
- [PartRenderer.Instruction.stop](partrenderer/instruction/stop.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/instruction)*