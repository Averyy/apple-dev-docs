# VNNormalizedPointForImagePoint(_:_:_:)

**Framework**: Vision  
**Kind**: func  
**Role**: Function

Projects a point from image coordinates into normalized coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func VNNormalizedPointForImagePoint(_ imagePoint: CGPoint, _ imageWidth: Int, _ imageHeight: Int) -> CGPoint
```

```c
extern CGPoint VNNormalizedPointForImagePoint(CGPoint imagePoint, size_t imageWidth, size_t imageHeight);
```

## Return Value

The input point projected into normalized coordinates.

## Discussion

The resulting point in image coordinate space may have nonintegral (floating-point) coordinates.

## Parameters

- `imagePoint`: The input point in image coordinate space.
- `imageWidth`: The image width.
- `imageHeight`: The image height.

## See Also

### Coordinate conversion
- [func VNImagePointForNormalizedPoint(CGPoint, Int, Int) -> CGPoint](./vnimagepointfornormalizedpoint%28_,_,_%29.md)
  Projects a point in normalized coordinates into image coordinates.
- [func VNImagePointForNormalizedPointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](./vnimagepointfornormalizedpointusingregionofinterest%28_,_,_,_%29.md)
  Projects a point from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](./vnnormalizedpointforimagepointusingregionofinterest%28_,_,_,_%29.md)
  Projects a point from a region of interest within the image coordinates into normalized coordinates.
- [func VNImageRectForNormalizedRect(CGRect, Int, Int) -> CGRect](./vnimagerectfornormalizedrect%28_,_,_%29.md)
  Projects a rectangle from normalized coordinates into image coordinates.
- [func VNNormalizedRectForImageRect(CGRect, Int, Int) -> CGRect](./vnnormalizedrectforimagerect%28_,_,_%29.md)
  Projects a rectangle from image coordinates into normalized coordinates.
- [func VNImageRectForNormalizedRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](./vnimagerectfornormalizedrectusingregionofinterest%28_,_,_,_%29.md)
  Projects a rectangle from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedRectForImageRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](./vnnormalizedrectforimagerectusingregionofinterest%28_,_,_,_%29.md)
  Projects a rectangle from a region of interest within the image coordinates space into normalized coordinates.
- [let VNNormalizedIdentityRect: CGRect](./vnnormalizedidentityrect.md)
  A normalized identity rectangle with an origin of zero and unit length and width.
- [func VNNormalizedRectIsIdentityRect(CGRect) -> Bool](./vnnormalizedrectisidentityrect%28_%29.md)
  Returns a Boolean value that indicates whether the rectangle has an origin of zero and unit length and width.
- [func VNImagePointForFaceLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](./vnimagepointforfacelandmarkpoint%28_,_,_,_%29.md)
  Returns the image coordinates of a specified face landmark point.
- [func VNNormalizedFaceBoundingBoxPointForLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](./vnnormalizedfaceboundingboxpointforlandmarkpoint%28_,_,_,_%29.md)
  Returns the coordinates of a specified face landmark point, in bounding box coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnnormalizedpointforimagepoint(_:_:_:))*