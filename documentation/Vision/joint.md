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
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DetectHumanBodyPoseRequest](detecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [struct DetectHumanHandPoseRequest](detecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [enum Chirality](chirality.md)
  The hand sidedness of a pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/joint)*