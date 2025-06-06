# VNImageRectForNormalizedRectUsingRegionOfInterest(_:_:_:_:)

**Framework**: Vision  
**Kind**: func

Projects a rectangle from a region of interest within the normalized coordinates into image coordinates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func VNImageRectForNormalizedRectUsingRegionOfInterest(_ normalizedRect: CGRect, _ imageWidth: Int, _ imageHeight: Int, _ roi: CGRect) -> CGRect
```

#### Return Value

A rectangle in the image-coordinate space.

## Parameters

- `normalizedRect`: The rectangle in normalized coordinates.
- `imageWidth`: The width of the image.
- `imageHeight`: The height of the image.
- `roi`: The region of interest within the normalized-coordinate space.

## See Also

- [func VNImagePointForNormalizedPoint(CGPoint, Int, Int) -> CGPoint](vnimagepointfornormalizedpoint(_:_:_:).md)
  Projects a point in normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePoint(CGPoint, Int, Int) -> CGPoint](vnnormalizedpointforimagepoint(_:_:_:).md)
  Projects a point from image coordinates into normalized coordinates.
- [func VNImagePointForNormalizedPointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](vnimagepointfornormalizedpointusingregionofinterest(_:_:_:_:).md)
  Projects a point from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](vnnormalizedpointforimagepointusingregionofinterest(_:_:_:_:).md)
  Projects a point from a region of interest within the image coordinates into normalized coordinates.
- [func VNImageRectForNormalizedRect(CGRect, Int, Int) -> CGRect](vnimagerectfornormalizedrect(_:_:_:).md)
  Projects a rectangle from normalized coordinates into image coordinates.
- [func VNNormalizedRectForImageRect(CGRect, Int, Int) -> CGRect](vnnormalizedrectforimagerect(_:_:_:).md)
  Projects a rectangle from image coordinates into normalized coordinates.
- [func VNNormalizedRectForImageRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](vnnormalizedrectforimagerectusingregionofinterest(_:_:_:_:).md)
  Projects a rectangle from a region of interest within the image coordinates space into normalized coordinates.
- [let VNNormalizedIdentityRect: CGRect](vnnormalizedidentityrect.md)
  A normalized identity rectangle with an origin of zero and unit length and width.
- [func VNNormalizedRectIsIdentityRect(CGRect) -> Bool](vnnormalizedrectisidentityrect(_:).md)
  Returns a Boolean value that indicates whether the rectangle has an origin of zero and unit length and width.
- [func VNImagePointForFaceLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](vnimagepointforfacelandmarkpoint(_:_:_:_:).md)
  Returns the image coordinates of a specified face landmark point.
- [func VNNormalizedFaceBoundingBoxPointForLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](vnnormalizedfaceboundingboxpointforlandmarkpoint(_:_:_:_:).md)
  Returns the coordinates of a specified face landmark point, in bounding box coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerectfornormalizedrectusingregionofinterest(_:_:_:_:))*