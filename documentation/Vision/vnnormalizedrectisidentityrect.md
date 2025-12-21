# VNNormalizedRectIsIdentityRect(_:)

**Framework**: Vision  
**Kind**: func

Returns a Boolean value that indicates whether the rectangle has an origin of zero and unit length and width.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func VNNormalizedRectIsIdentityRect(_ normalizedRect: CGRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the rectangle is the identity rectangle, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `normalizedRect`: Normalized input rect to test for identity.

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
- [func VNImageRectForNormalizedRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](vnimagerectfornormalizedrectusingregionofinterest(_:_:_:_:).md)
  Projects a rectangle from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedRectForImageRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](vnnormalizedrectforimagerectusingregionofinterest(_:_:_:_:).md)
  Projects a rectangle from a region of interest within the image coordinates space into normalized coordinates.
- [let VNNormalizedIdentityRect: CGRect](vnnormalizedidentityrect.md)
  A normalized identity rectangle with an origin of zero and unit length and width.
- [func VNImagePointForFaceLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](vnimagepointforfacelandmarkpoint(_:_:_:_:).md)
  Returns the image coordinates of a specified face landmark point.
- [func VNNormalizedFaceBoundingBoxPointForLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](vnnormalizedfaceboundingboxpointforlandmarkpoint(_:_:_:_:).md)
  Returns the coordinates of a specified face landmark point, in bounding box coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnnormalizedrectisidentityrect(_:))*