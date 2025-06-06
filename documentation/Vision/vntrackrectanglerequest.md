# VNTrackRectangleRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNTrackRectangleRequest
```

#### Overview

Use this type of request to track the bounding boxes of rectangles throughout a sequence of images. Vision returns locations for rectangles found in all orientations and sizes.

## Topics

### Initializing a Rectangle Tracking Request
- [convenience init(rectangleObservation: VNRectangleObservation)](vntrackrectanglerequest/init(rectangleobservation:).md)
  Creates a new rectangle tracking request with a rectangle observation.
- [init(rectangleObservation: VNRectangleObservation, completionHandler: VNRequestCompletionHandler?)](vntrackrectanglerequest/init(rectangleobservation:completionhandler:).md)
  Creates a new rectangle tracking request with a rectangle observation.
### Identifying Request Revisions
- [let VNTrackRectangleRequestRevision1: Int](vntrackrectanglerequestrevision1.md)
  A constant for specifying revision 1 of the rectangling tracking request.

## Relationships

### Inherits From
- [VNTrackingRequest](vntrackingrequest.md)
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
- [class VNTrackingRequest](vntrackingrequest.md)
  The abstract superclass for image-analysis requests that track unique features across multiple images or video frames.
- [class VNTrackObjectRequest](vntrackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- [class VNDetectedObjectObservation](vndetectedobjectobservation.md)
  An observation that provides the position and extent of an image feature that an image- analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackrectanglerequest)*