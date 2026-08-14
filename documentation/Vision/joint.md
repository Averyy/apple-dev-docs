# Joint

**Framework**: Vision  
**Kind**: struct

A pose joint represented as a normalized point in an image, along with a label and a confidence value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Joint
```

## Topics

### Inspecting a joint
- [let confidence: Float](joint/confidence.md)
  A confidence score that indicates the detected joint’s accuracy.
- [let jointName: String](joint/jointname.md)
  The joint’s identifier label.
- [let location: NormalizedPoint](joint/location.md)
  The location of the joint in normalized coordinates.
### Getting the distance to a joint
- [func distance(to: Joint) -> CGFloat](joint/distance(to:).md)
  Returns the distance to another joint.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Joint3D](joint3d.md)
  An object that represents a body pose joint in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/joint)*