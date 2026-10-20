# PartRenderer.Instruction

**Framework**: hvf  
**Kind**: enum  
**Role**: Enumeration

The set of instructions passed to a render context

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
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
- [case addCubic(cp1: PartRenderer.Point, cp2: PartRenderer.Point, on: PartRenderer.Point)](./instruction/addcubic%28cp1,cp2,on%29.md)
- [PartRenderer.Instruction.addLine(_:)](./instruction/addline%28_%29.md)
- [PartRenderer.Instruction.addPoint(_:)](./instruction/addpoint%28_%29.md)
- [case addQuad(off: PartRenderer.Point, on: PartRenderer.Point)](./instruction/addquad%28off,on%29.md)
- [PartRenderer.Instruction.beginPart(id:name:)](./instruction/beginpart%28id,name%29.md)
  The name value is for client use and is not set by the loader or scaler
- [PartRenderer.Instruction.beginPath](./instruction/beginpath.md)
- [PartRenderer.Instruction.closePath](./instruction/closepath.md)
- [PartRenderer.Instruction.endPart(id:name:)](./instruction/endpart%28id,name%29.md)
  The name value is for client use and is not set by the loader or scaler
- [PartRenderer.Instruction.endPath](./instruction/endpath.md)
- [PartRenderer.Instruction.stop](./instruction/stop.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/instruction)*