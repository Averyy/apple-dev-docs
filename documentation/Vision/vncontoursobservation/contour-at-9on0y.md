# contour(at:)

**Framework**: Vision  
**Kind**: method

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

#### Return Value

The contour object at the specified index.

## Parameters

- `contourIndex`: The index of the contour to retrieve. Valid values are in the range of 0 to   - 1.

## See Also

- [var contourCount: Int](vncontoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](vncontoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [VNContour]](vncontoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
- [var topLevelContourCount: Int](vncontoursobservation/toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: IndexPath) throws -> VNContour](vncontoursobservation/contour(at:)-52odo.md)
  Retrieves the contour object at the specified index path.
- [class VNContour](vncontour.md)
  A class that represents a detected contour in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation/contour(at:)-9on0y)*