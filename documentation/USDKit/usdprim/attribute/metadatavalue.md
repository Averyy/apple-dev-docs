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

Types that conform to this protocol can be read and written as metadata using [`USDStage`](usdstage-4sfi1.md) and [`USDStage.Object.MetadataCollection`](usdstage-4sfi1/object/metadatacollection.md).

> ❗ **Important**: Don’t declare new conformances to `MetadataValue`. Only the types already supported by the USDKit framework are valid conforming types.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [USDToken](usdtoken.md)
- [USDValue.Vec3d](usdvalue/vec3d.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/metadatavalue)*