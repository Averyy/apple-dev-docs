# VNRequestTrackingLevel

**Framework**: Vision  
**Kind**: enum

An enumeration of tracking priorities.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum VNRequestTrackingLevel
```

## Topics

### Enumeration Cases
- [VNRequestTrackingLevel.accurate](vnrequesttrackinglevel/accurate.md)
  Tracking level that favors location accuracy over speed.
- [VNRequestTrackingLevel.fast](vnrequesttrackinglevel/fast.md)
  Tracking level that favors speed over location accuracy.
### Creating a Tracking Level
- [init?(rawValue: UInt)](vnrequesttrackinglevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var inputObservation: VNDetectedObjectObservation](vntrackingrequest/inputobservation.md)
  The observation object defining a region to track.
- [var trackingLevel: VNRequestTrackingLevel](vntrackingrequest/trackinglevel.md)
  A value for specifying whether to prioritize speed or location accuracy.
- [var isLastFrame: Bool](vntrackingrequest/islastframe.md)
  A Boolean that indicates the last frame in a tracking sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequesttrackinglevel)*