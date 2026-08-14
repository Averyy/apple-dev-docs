# USDValue.Vec4i

**Framework**: USDKit  
**Kind**: struct

A 4-component 32-bit integer vector.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Vec4i
```

## Topics

### Initializers
- [init()](usdvalue/vec4i/init.md)
  Creates a zero vector.
- [init(SIMD4<Int32>)](usdvalue/vec4i/init(_:).md)
  Creates a vector from a `SIMD4<Int32>`.
- [init(Int, Int, Int, Int)](usdvalue/vec4i/init(_:_:_:_:)-5ou3l.md)
  Creates a vector with the given components.
- [init(Int32, Int32, Int32, Int32)](usdvalue/vec4i/init(_:_:_:_:)-80hw8.md)
### Instance Properties
- [var simd: SIMD4<Int32>](usdvalue/vec4i/simd.md)
  The vector as a `SIMD4<Int32>`.
- [var w: Int32](usdvalue/vec4i/w.md)
- [var x: Int32](usdvalue/vec4i/x.md)
- [var y: Int32](usdvalue/vec4i/y.md)
- [var z: Int32](usdvalue/vec4i/z.md)
### Subscripts
- [subscript(Int) -> Int32](usdvalue/vec4i/subscript(_:).md)
  Accesses the component at the specified index.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec4i)*