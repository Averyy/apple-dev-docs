# isLastFrame

**Framework**: Vision  
**Kind**: property

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

#### Discussion

If set to [`true`](https://developer.apple.com/documentation/swift/true), the current tracker will be released to the pool of available trackers when the current frame finishes processing.

## See Also

- [enum VNRequestTrackingLevel](vnrequesttrackinglevel.md)
  An enumeration of tracking priorities.
- [var inputObservation: VNDetectedObjectObservation](vntrackingrequest/inputobservation.md)
  The observation object defining a region to track.
- [var trackingLevel: VNRequestTrackingLevel](vntrackingrequest/trackinglevel.md)
  A value for specifying whether to prioritize speed or location accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackingrequest/islastframe)*