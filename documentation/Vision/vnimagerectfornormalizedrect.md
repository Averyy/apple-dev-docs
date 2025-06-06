# VNImageRectForNormalizedRect(_:_:_:)

**Framework**: Vision  
**Kind**: func

Projects a rectangle from normalized coordinates into image coordinates.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func VNImageRectForNormalizedRect(_ normalizedRect: CGRect, _ imageWidth: Int, _ imageHeight: Int) -> CGRect
```

## Mentions

- [Recognizing Text in Images](recognizing-text-in-images.md)

#### Return Value

The input rect projected into image (pixel) coordinates.

## Parameters

- `normalizedRect`: The input rectangle in normalized coordinate space.
- `imageWidth`: The width of the image into whose coordinate space you’re projecting the input rect.
- `imageHeight`: The height of the image into whose coordinate space you’re projecting the input rect.

## See Also

- [func VNImagePointForNormalizedPoint(CGPoint, Int, Int) -> CGPoint](vnimagepointfornormalizedpoint(_:_:_:).md)
  Projects a point in normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePoint(CGPoint, Int, Int) -> CGPoint](vnnormalizedpointforimagepoint(_:_:_:).md)
  Projects a point from image coordinates into normalized coordinates.
- [func VNImagePointForNormalizedPointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](vnimagepointfornormalizedpointusingregionofinterest(_:_:_:_:).md)
  Projects a point from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](vnnormalizedpointforimagepointusingregionofinterest(_:_:_:_:).md)
  Projects a point from a region of interest within the image coordinates into normalized coordinates.
- [func VNNormalizedRectForImageRect(CGRect, Int, Int) -> CGRect](vnnormalizedrectforimagerect(_:_:_:).md)
  Projects a rectangle from image coordinates into normalized coordinates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerectfornormalizedrect(_:_:_:))*