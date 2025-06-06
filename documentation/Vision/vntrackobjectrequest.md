# VNTrackObjectRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNTrackObjectRequest
```

#### Overview

Use this type of request to track the bounding boxes around objects previously identified in an image. Vision attempts to locate the same object from the input observation throughout the sequence.

## Topics

### Initializing an Object Tracking Request
- [init(detectedObjectObservation: VNDetectedObjectObservation)](vntrackobjectrequest/init(detectedobjectobservation:).md)
  Creates a new object tracking request with a detected object observation.
- [init(detectedObjectObservation: VNDetectedObjectObservation, completionHandler: VNRequestCompletionHandler?)](vntrackobjectrequest/init(detectedobjectobservation:completionhandler:).md)
  Creates a new object tracking request with a detected object observation.
### Identifying Request Revisions
- [let VNTrackObjectRequestRevision2: Int](vntrackobjectrequestrevision2.md)
  A constant for specifying revision 2 of the object tracking request.
- [let VNTrackObjectRequestRevision1: Int](vntrackobjectrequestrevision1.md)
  A constant for specifying revision 1 of the object tracking request.

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
- [class VNTrackRectangleRequest](vntrackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.
- [class VNDetectedObjectObservation](vndetectedobjectobservation.md)
  An observation that provides the position and extent of an image feature that an image- analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackobjectrequest)*