# VNDetectRectanglesRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that finds projected rectangular regions in an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectRectanglesRequest
```

#### Overview

A rectangle detection request locates regions of an image with rectangular shape, like credit cards, business cards, documents, and signs. The request returns its observations in the form of [`VNRectangleObservation`](vnrectangleobservation.md) objects, which contain normalized coordinates of bounding boxes containing the rectangle.

Use this type of request to find the bounding boxes of rectangles in an image. Vision returns observations for rectangles found in all orientations and sizes, along with a confidence level to indicate how likely it’s that the observation contains an actual rectangle.

To further configure or restrict the types of rectangles found, set properties on the request specifying a range of aspect ratios, sizes, and quadrature tolerance.

## Topics

### Configuring Detection
- [var minimumAspectRatio: VNAspectRatio](vndetectrectanglesrequest/minimumaspectratio.md)
  A `float` specifying the minimum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [var maximumAspectRatio: VNAspectRatio](vndetectrectanglesrequest/maximumaspectratio.md)
  A `float` specifying the maximum aspect ratio of the rectangle to detect, defined as the shorter dimension over the longer dimension.
- [typealias VNAspectRatio](vnaspectratio.md)
  A type alias for expressing rectangle aspect ratios in Vision.
- [var quadratureTolerance: VNDegrees](vndetectrectanglesrequest/quadraturetolerance.md)
  A float specifying the number of degrees a rectangle corner angle can deviate from 90°.
- [typealias VNDegrees](vndegrees.md)
  A typealias for expressing tolerance angles in Vision.
- [var minimumSize: Float](vndetectrectanglesrequest/minimumsize.md)
  The minimum size of a rectangle to detect, as a proportion of the smallest dimension.
- [var minimumConfidence: VNConfidence](vndetectrectanglesrequest/minimumconfidence.md)
  A value specifying the minimum acceptable confidence level.
- [typealias VNConfidence](vnconfidence.md)
  A type alias for the confidence value of an observation.
- [var maximumObservations: Int](vndetectrectanglesrequest/maximumobservations.md)
  An integer specifying the maximum number of rectangles Vision returns.
### Accessing the Results
- [var results: [VNRectangleObservation]?](vndetectrectanglesrequest/results.md)
  The results of the request to detect rectangles.
- [class VNRectangleObservation](vnrectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.
### Identifying Request Revisions
- [let VNDetectRectanglesRequestRevision1: Int](vndetectrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the rectangle detection request.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectrectanglesrequest)*