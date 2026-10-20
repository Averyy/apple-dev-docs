# USDPrim.Attribute.ValueType.TupleDimensions

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

The shape of a value type’s components.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
- [USDPrim.Attribute.ValueType.TupleDimensions.matrix(rows:columns:)](./tupledimensions/matrix%28rows,columns%29.md)
- [USDPrim.Attribute.ValueType.TupleDimensions.scalar](./tupledimensions/scalar.md)
- [USDPrim.Attribute.ValueType.TupleDimensions.vector(_:)](./tupledimensions/vector%28_%29.md)
### Instance Properties
- [var componentCount: Int](./tupledimensions/componentcount.md)
  The total number of components across all dimensions.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/valuetype/tupledimensions)*