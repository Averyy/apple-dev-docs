# VNNormalizedRectForImageRect(_:_:_:)

**Framework**: Vision  
**Kind**: func

Projects a rectangle from image coordinates into normalized coordinates.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func VNNormalizedRectForImageRect(_ imageRect: CGRect, _ imageWidth: Int, _ imageHeight: Int) -> CGRect
```

#### Return Value

The input rectangle projected into normalized coordinates.

## Parameters

- `imageRect`: The input rectangle in image coordinate space.
- `imageWidth`: The width of the image in whose coordinates the input rect resides.
- `imageHeight`: The height of the image in whose coordinates the input rect resides.

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
- [func VNImageRectForNormalizedRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](vnimagerectfornormalizedrectusingregionofinterest(_:_:_:_:).md)
  Projects a rectangle from a region of interest within the normalized coordinates into image coordinates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnnormalizedrectforimagerect(_:_:_:))*