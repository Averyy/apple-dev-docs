# isLastFrame

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates the last frame in a tracking sequence.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isLastFrame: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isLastFrame) BOOL lastFrame;
```

## Discussion

If set to [`true`](../../Swift/true.md), the current tracker will be released to the pool of available trackers when the current frame finishes processing.

## See Also

### Configuring a Tracking Request
- [enum VNRequestTrackingLevel](../vnrequesttrackinglevel.md)
  An enumeration of tracking priorities.
- [var inputObservation: VNDetectedObjectObservation](./inputobservation.md)
  The observation object defining a region to track.
- [var trackingLevel: VNRequestTrackingLevel](./trackinglevel.md)
  A value for specifying whether to prioritize speed or location accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackingrequest/islastframe)*