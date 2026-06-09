# USDPrim.Attribute.Value

**Framework**: USDKit  
**Kind**: protocol

A value that can be stored on an attribute in a Universal Scene Description file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Value : Sendable
```

#### Overview

Types that conform to this protocol can be authored as an attribute value using [`USDPrim`](usdprim.md), `USDPrim.Attribute`, or [`USDLayer`](usdlayer.md).

> ❗ **Important**: Don’t declare new conformances to `USDPrim.Attribute.Value`. Only the types already supported by the USDKit framework are valid conforming types.

## Topics

### Type Properties
- [static var valueType: USDPrim.Attribute.ValueType](usdprim/attribute/value/valuetype.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [USDLayer.AssetPath](usdlayer/assetpath.md)
- [USDLayer.PathExpression](usdlayer/pathexpression.md)
- [USDLayer.TimeCode](usdlayer/timecode.md)
- [USDToken](usdtoken.md)
- [USDValue.Vec3d](usdvalue/vec3d.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/value)*