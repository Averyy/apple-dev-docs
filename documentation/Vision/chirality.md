# Chirality

**Framework**: Vision  
**Kind**: enum

The hand sidedness of a pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Chirality
```

## Topics

### Getting the hand sidedness
- [Chirality.left](chirality/left.md)
  A case that represents the left hand.
- [Chirality.right](chirality/right.md)
  A case that represents the right hand.

## Relationships

### Conforms To
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
- [struct Joint](joint.md)
  A pose joint represented as a normalized point in an image, along with a label and a confidence value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/chirality)*