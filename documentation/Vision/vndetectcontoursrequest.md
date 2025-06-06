# VNDetectContoursRequest

**Framework**: Vision  
**Kind**: class

A request that detects the contours of the edges of an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectContoursRequest
```

## Topics

### Configuring the Request
- [var contrastAdjustment: Float](vndetectcontoursrequest/contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var contrastPivot: NSNumber?](vndetectcontoursrequest/contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](vndetectcontoursrequest/detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var maximumImageDimension: Int](vndetectcontoursrequest/maximumimagedimension.md)
  The maximum image dimension to use for contour detection.
- [var detectDarkOnLight: Bool](vndetectcontoursrequest/detectdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background.
### Accessing the Results
- [var results: [VNContoursObservation]?](vndetectcontoursrequest/results.md)
  The results of the request to detect contours.
- [class VNContoursObservation](vncontoursobservation.md)
  An object that represents the detected contours in an image.
### Identifying Request Revisions
- [let VNDetectContourRequestRevision1: Int](vndetectcontourrequestrevision1.md)
  A constant for specifying revision 1 of the contours detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectcontoursrequest)*