# USDPrim.Attribute.ValueType.TupleDimensions

**Framework**: USDKit  
**Kind**: enum

The shape of a value type’s components.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum TupleDimensions
```

#### Overview

- `scalar`: a single value (e.g. `Float`, `Int`).
- `vector(n)`: an n-component tuple (e.g. `Float3` is `.vector(3)`).
- `matrix(rows:cols:)`: a 2D tuple (e.g. `Matrix4d` is `.matrix(rows: 4, cols: 4)`).

## Topics

### Enumeration Cases
- [USDPrim.Attribute.ValueType.TupleDimensions.matrix(rows:columns:)](usdprim/attribute/valuetype/tupledimensions/matrix(rows:columns:).md)
- [USDPrim.Attribute.ValueType.TupleDimensions.scalar](usdprim/attribute/valuetype/tupledimensions/scalar.md)
- [USDPrim.Attribute.ValueType.TupleDimensions.vector(_:)](usdprim/attribute/valuetype/tupledimensions/vector(_:).md)
### Instance Properties
- [var componentCount: Int](usdprim/attribute/valuetype/tupledimensions/componentcount.md)
  The total number of components across all dimensions.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/valuetype/tupledimensions)*