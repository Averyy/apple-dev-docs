# VNChirality

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Constants that the define the chirality, or handedness, of a pose.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@frozen
enum VNChirality
```

```c
enum VNChirality : NSInteger;
```

## Topics

### Chirality Values
- [VNChirality.left](./vnchirality/left.md)
  Indicates a left-handed pose.
- [VNChirality.right](./vnchirality/right.md)
  Indicates a right-handed pose.
- [VNChirality.unknown](./vnchirality/unknown.md)
  Indicates that the pose chirality is unknown.
### Creating a Chirality
- [init?(rawValue: Int)](./vnchirality/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining the Chirality
- [var chirality: VNChirality](./vnhumanhandposeobservation/chirality.md)
  The chirality, or handedness, of a pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnchirality)*