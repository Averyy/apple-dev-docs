# USDTransformOperation

**Framework**: USDKit  
**Kind**: struct

A single transform applied to a prim, such as a translation, rotation, scale, or matrix.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDTransformOperation
```

## Topics

### Initializers
- [init(attribute: USDPrim.Attribute, inverted: Bool)](usdtransformoperation/init(attribute:inverted:).md)
  Creates a transform operation from an attribute.
### Instance Properties
- [var attribute: USDPrim.Attribute](usdtransformoperation/attribute.md)
  The attribute backing this operation.
- [var baseName: USDToken](usdtransformoperation/basename.md)
  The base name of this operation without namespace.
- [var hasTimeSamples: Bool](usdtransformoperation/hastimesamples.md)
  A Boolean value indicating whether the operation has authored time samples.
- [var isDefined: Bool](usdtransformoperation/isdefined.md)
  A Boolean value indicating whether this operation is defined.
- [var isInverse: Bool](usdtransformoperation/isinverse.md)
  A Boolean value indicating whether this is an inverse operation.
- [var kind: USDTransformOperation.Kind?](usdtransformoperation/kind-swift.property.md)
  The kind of this transform operation, or `nil` if the operation is not defined.
- [var name: USDToken](usdtransformoperation/name.md)
  The full name of this operation.
- [var precision: USDTransformOperation.Precision](usdtransformoperation/precision-swift.property.md)
  The numeric precision of this operation’s value.
- [var timeSamples: [USDStage.TimeCode]](usdtransformoperation/timesamples.md)
  All time samples authored for this operation.
### Instance Methods
- [func timeSamples(in: ClosedRange<USDStage.TimeCode>) -> [USDStage.TimeCode]](usdtransformoperation/timesamples(in:).md)
  Returns time samples authored within the specified interval.
- [func transform(at: USDStage.TimeCode) -> USDValue.Matrix4d](usdtransformoperation/transform(at:).md)
  Computes the transformation matrix at the specified time.
### Enumerations
- [USDTransformOperation.Kind](usdtransformoperation/kind-swift.enum.md)
  The kind of transform operation.
- [USDTransformOperation.Precision](usdtransformoperation/precision-swift.enum.md)
  The numeric precision of the operation’s value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtransformoperation)*