# VNRequestTrackingLevel

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

An enumeration of tracking priorities.

## Declaration

```swift
enum VNRequestTrackingLevel
```

```c
enum VNRequestTrackingLevel : NSUInteger;
```

## Topics

### Enumeration Cases
- [VNRequestTrackingLevel.accurate](./vnrequesttrackinglevel/accurate.md)
  Tracking level that favors location accuracy over speed.
- [VNRequestTrackingLevel.fast](./vnrequesttrackinglevel/fast.md)
  Tracking level that favors speed over location accuracy.
### Creating a Tracking Level
- [init?(rawValue: UInt)](./vnrequesttrackinglevel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a Tracking Request
- [var inputObservation: VNDetectedObjectObservation](./vntrackingrequest/inputobservation.md)
  The observation object defining a region to track.
- [var trackingLevel: VNRequestTrackingLevel](./vntrackingrequest/trackinglevel.md)
  A value for specifying whether to prioritize speed or location accuracy.
- [var isLastFrame: Bool](./vntrackingrequest/islastframe.md)
  A Boolean that indicates the last frame in a tracking sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequesttrackinglevel)*