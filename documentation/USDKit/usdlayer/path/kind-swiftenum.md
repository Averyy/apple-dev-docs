# USDLayer.Path.Kind

**Framework**: USDKit  
**Kind**: enum

The classification of the path’s leaf element.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [USDLayer.Path.Kind.absoluteRoot](usdlayer/path/kind-swift.enum/absoluteroot.md)
  The path is the absolute root, `/`.
- [USDLayer.Path.Kind.empty](usdlayer/path/kind-swift.enum/empty.md)
  The path is empty.
- [USDLayer.Path.Kind.expression](usdlayer/path/kind-swift.enum/expression.md)
  Connection expression path. Legacy USD syntax retained for classifying paths parsed from older USDA data.
- [USDLayer.Path.Kind.mapper](usdlayer/path/kind-swift.enum/mapper.md)
  Connection mapper path. Legacy USD syntax retained for classifying paths parsed from older USDA data.
- [USDLayer.Path.Kind.mapperArgument](usdlayer/path/kind-swift.enum/mapperargument.md)
  Mapper-argument path. Legacy USD syntax retained for classifying paths parsed from older USDA data.
- [USDLayer.Path.Kind.prim](usdlayer/path/kind-swift.enum/prim.md)
  The path identifies a prim.
- [USDLayer.Path.Kind.primVariantSelection](usdlayer/path/kind-swift.enum/primvariantselection.md)
  The path is a variant selection.
- [USDLayer.Path.Kind.property](usdlayer/path/kind-swift.enum/property.md)
  The path identifies a property on a prim or relationship target.
- [USDLayer.Path.Kind.target](usdlayer/path/kind-swift.enum/target.md)
  The path is a relationship target.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/path/kind-swift.enum)*