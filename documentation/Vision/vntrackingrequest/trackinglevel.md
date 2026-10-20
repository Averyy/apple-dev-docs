# trackingLevel

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A value for specifying whether to prioritize speed or location accuracy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var trackingLevel: VNRequestTrackingLevel { get set }
```

```objc
@property (nonatomic, assign, readwrite) VNRequestTrackingLevel trackingLevel;
```

## See Also

### Configuring a Tracking Request
- [enum VNRequestTrackingLevel](../vnrequesttrackinglevel.md)
  An enumeration of tracking priorities.
- [var inputObservation: VNDetectedObjectObservation](./inputobservation.md)
  The observation object defining a region to track.
- [var isLastFrame: Bool](./islastframe.md)
  A Boolean that indicates the last frame in a tracking sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackingrequest/trackinglevel)*