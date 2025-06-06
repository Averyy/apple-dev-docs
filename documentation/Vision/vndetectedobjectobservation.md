# VNDetectedObjectObservation

**Framework**: Vision  
**Kind**: class

An observation that provides the position and extent of an image feature that an image- analysis request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectedObjectObservation
```

#### Overview

This class is the observation type that [`VNTrackObjectRequest`](vntrackobjectrequest.md) generates. It represents an object that the Vision request detects and tracks.

## Topics

### Creating an Observation
- [convenience init(boundingBox: CGRect)](vndetectedobjectobservation/init(boundingbox:).md)
  Creates an observation with a bounding box.
- [convenience init(requestRevision: Int, boundingBox: CGRect)](vndetectedobjectobservation/init(requestrevision:boundingbox:).md)
  Creates an observation with a revision number and bounding box.
### Locating a Detected Object
- [var boundingBox: CGRect](vndetectedobjectobservation/boundingbox.md)
  The bounding box of the object that the request detects.
### Accessing an Image Mask
- [var globalSegmentationMask: VNPixelBufferObservation?](vndetectedobjectobservation/globalsegmentationmask.md)
  A resulting pixel buffer from a request to generate a segmentation mask for an image.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Inherited By
- [VNFaceObservation](vnfaceobservation.md)
- [VNHumanObservation](vnhumanobservation.md)
- [VNRecognizedObjectObservation](vnrecognizedobjectobservation.md)
- [VNRectangleObservation](vnrectangleobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Tracking the User’s Face in Real Time](tracking-the-user-s-face-in-real-time.md)
  Detect and track faces from the selfie cam feed in real time.
- [Tracking Multiple Objects or Rectangles in Video](tracking-multiple-objects-or-rectangles-in-video.md)
  Apply Vision algorithms to track objects or rectangles throughout a video.
- [class VNTrackingRequest](vntrackingrequest.md)
  The abstract superclass for image-analysis requests that track unique features across multiple images or video frames.
- [class VNTrackRectangleRequest](vntrackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.
- [class VNTrackObjectRequest](vntrackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectedobjectobservation)*