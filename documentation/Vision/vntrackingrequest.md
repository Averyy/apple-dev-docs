# VNTrackingRequest

**Framework**: Vision  
**Kind**: class

The abstract superclass for image-analysis requests that track unique features across multiple images or video frames.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNTrackingRequest
```

#### Overview

Instantiate a tracking request subclass to perform object tracking across multiple frames of an image. After initialization, configure the degree of accuracy by setting [`trackingLevel`](vntrackingrequest/trackinglevel.md), and provide observations you’d like to track by setting the [`inputObservation`](vntrackingrequest/inputobservation.md) initial bounding box.

## Topics

### Configuring a Tracking Request
- [enum VNRequestTrackingLevel](vnrequesttrackinglevel.md)
  An enumeration of tracking priorities.
- [var inputObservation: VNDetectedObjectObservation](vntrackingrequest/inputobservation.md)
  The observation object defining a region to track.
- [var trackingLevel: VNRequestTrackingLevel](vntrackingrequest/trackinglevel.md)
  A value for specifying whether to prioritize speed or location accuracy.
- [var isLastFrame: Bool](vntrackingrequest/islastframe.md)
  A Boolean that indicates the last frame in a tracking sequence.
### Getting the Number of Trackers
- [func supportedNumber(ofTrackersAndReturnError: NSErrorPointer) -> Int](vntrackingrequest/supportednumber(oftrackersandreturnerror:).md)
  Returns the maximum number of simultaneous trackers for the request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Inherited By
- [VNTrackObjectRequest](vntrackobjectrequest.md)
- [VNTrackRectangleRequest](vntrackrectanglerequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Tracking the User’s Face in Real Time](tracking-the-user-s-face-in-real-time.md)
  Detect and track faces from the selfie cam feed in real time.
- [Tracking Multiple Objects or Rectangles in Video](tracking-multiple-objects-or-rectangles-in-video.md)
  Apply Vision algorithms to track objects or rectangles throughout a video.
- [class VNTrackRectangleRequest](vntrackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.
- [class VNTrackObjectRequest](vntrackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- [class VNDetectedObjectObservation](vndetectedobjectobservation.md)
  An observation that provides the position and extent of an image feature that an image- analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackingrequest)*