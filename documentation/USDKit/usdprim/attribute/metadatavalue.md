# USDPrim.Attribute.MetadataValue

**Framework**: USDKit  
**Kind**: protocol

A value that can be stored as metadata in a Universal Scene Description file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MetadataValue : Sendable
```

#### Overview

Types that conform to this protocol can be read and written as metadata using [`USDStage`](usdstage.md) and [`USDStage.Object.MetadataCollection`](usdstage/object/metadatacollection.md).

> ❗ **Important**: Don’t declare new conformances to `MetadataValue`. Only the types already supported by the USDKit framework are valid conforming types.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [USDToken](usdtoken.md)
- [USDValue.Matrix2d](usdvalue/matrix2d.md)
- [USDValue.Matrix3d](usdvalue/matrix3d.md)
- [USDValue.Matrix4d](usdvalue/matrix4d.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/metadatavalue)*