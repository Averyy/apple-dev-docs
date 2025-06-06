# inputObservation

**Framework**: Vision  
**Kind**: property

The observation object defining a region to track.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var inputObservation: VNDetectedObjectObservation { get set }
```

#### Discussion

Providing an observation not returned from a tracker, such as a user-defined observation, begins a new tracker for the sequence. Providing an observation that was returned from a tracker continues the use of that tracker, to track the region to the next frame.

In general, unless specified in the request’s documentation or header file, you must define the rectangle in normalized coordinates, with the origin at the lower-left corner.

## See Also

- [enum VNRequestTrackingLevel](vnrequesttrackinglevel.md)
  An enumeration of tracking priorities.
- [var trackingLevel: VNRequestTrackingLevel](vntrackingrequest/trackinglevel.md)
  A value for specifying whether to prioritize speed or location accuracy.
- [var isLastFrame: Bool](vntrackingrequest/islastframe.md)
  A Boolean that indicates the last frame in a tracking sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackingrequest/inputobservation)*