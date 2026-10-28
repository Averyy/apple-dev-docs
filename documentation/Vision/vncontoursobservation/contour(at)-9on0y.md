# contour(at:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Retrieves the contour object at the specified index, irrespective of hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func contour(at contourIndex: Int) throws -> VNContour
```

```objc
- (VNContour *) contourAtIndex:(NSInteger) contourIndex error:(NSError **) error;
```

## Return Value

The contour object at the specified index.

## Parameters

- `contourIndex`: The index of the contour to retrieve. Valid values are in the range of 0 to [`contourCount`](./contourcount.md) - 1.

## See Also

### Inspecting the Observation
- [var contourCount: Int](./contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](./normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [VNContour]](./toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
- [var topLevelContourCount: Int](./toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: IndexPath) throws -> VNContour](./contour%28at%29-52odo.md)
  Retrieves the contour object at the specified index path.
- [class VNContour](../vncontour.md)
  A class that represents a detected contour in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation/contour(at:)-9on0y)*