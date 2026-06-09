# USDValueProtocol

**Framework**: USDKit  
**Kind**: protocol

A type that can be wrapped in a [`USDValue`](usdvalue.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol USDValueProtocol
```

#### Overview

Types that conform to this protocol can be stored in and retrieved from a [`USDValue`](usdvalue.md).

> ❗ **Important**: Don’t declare new conformances to `USDValueProtocol`. Only the types already supported by the USDKit framework are valid conforming types.

## Relationships

### Conforming Types
- [USDLayer.AssetPath](usdlayer/assetpath.md)
- [USDLayer.ListOperation](usdlayer/listoperation.md)
- [USDLayer.Path](usdlayer/path.md)
- [USDLayer.PathExpression](usdlayer/pathexpression.md)
- [USDLayer.Permission](usdlayer/permission.md)
- [USDLayer.TimeCode](usdlayer/timecode.md)
- [USDLayer.TimeOffset](usdlayer/timeoffset.md)
- [USDPrim.Property.Variability](usdprim/property/variability.md)
- [USDPrim.Specifier](usdprim/specifier-swift.enum.md)
- [USDToken](usdtoken.md)
- [USDValue.Vec3d](usdvalue/vec3d.md)

## See Also

- [struct USDValue](usdvalue.md)
  A type-erased container for a value stored in a Universal Scene Description file.
- [struct USDToken](usdtoken.md)
  An interned, efficiently compared string that names prims, properties, and other scene-description identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalueprotocol)*