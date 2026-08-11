# USDValue.Vec2i

**Framework**: USDKit  
**Kind**: struct

A 2-component 32-bit integer vector.

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
struct Vec2i
```

## Topics

### Initializers
- [init()](usdvalue/vec2i/init.md)
  Creates a zero vector.
- [init(SIMD2<Int32>)](usdvalue/vec2i/init(_:).md)
  Creates a vector from a `SIMD2<Int32>`.
- [init(Int32, Int32)](usdvalue/vec2i/init(_:_:)-7uw95.md)
- [init(Int, Int)](usdvalue/vec2i/init(_:_:)-8faxo.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Int32>](usdvalue/vec2i/simd.md)
  The vector as a `SIMD2<Int32>`.
- [var x: Int32](usdvalue/vec2i/x.md)
- [var y: Int32](usdvalue/vec2i/y.md)
### Subscripts
- [subscript(Int) -> Int32](usdvalue/vec2i/subscript(_:).md)
  Accesses the component at the specified index.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2i)*