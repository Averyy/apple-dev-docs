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
- [USDValue.Matrix2d](usdvalue/matrix2d.md)
- [USDValue.Matrix2f](usdvalue/matrix2f.md)
- [USDValue.Matrix3d](usdvalue/matrix3d.md)
- [USDValue.Matrix3f](usdvalue/matrix3f.md)
- [USDValue.Matrix4d](usdvalue/matrix4d.md)
- [USDValue.Matrix4f](usdvalue/matrix4f.md)
- [USDValue.Quatd](usdvalue/quatd.md)
- [USDValue.Quatf](usdvalue/quatf.md)
- [USDValue.Quath](usdvalue/quath.md)
- [USDValue.Vec2d](usdvalue/vec2d.md)
- [USDValue.Vec2f](usdvalue/vec2f.md)
- [USDValue.Vec2h](usdvalue/vec2h.md)
- [USDValue.Vec2i](usdvalue/vec2i.md)
- [USDValue.Vec3d](usdvalue/vec3d.md)
- [USDValue.Vec3f](usdvalue/vec3f.md)
- [USDValue.Vec3h](usdvalue/vec3h.md)
- [USDValue.Vec3i](usdvalue/vec3i.md)
- [USDValue.Vec4d](usdvalue/vec4d.md)
- [USDValue.Vec4f](usdvalue/vec4f.md)
- [USDValue.Vec4h](usdvalue/vec4h.md)
- [USDValue.Vec4i](usdvalue/vec4i.md)

## See Also

- [struct USDValue](usdvalue.md)
  A type-erased container for a value stored in a Universal Scene Description file.
- [struct USDToken](usdtoken.md)
  An interned, efficiently compared string that names prims, properties, and other scene-description identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalueprotocol)*