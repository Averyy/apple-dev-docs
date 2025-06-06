# contour(at:)

**Framework**: Vision  
**Kind**: method

Retrieves the contour object at the specified index path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func contour(at indexPath: IndexPath) throws -> VNContour
```

#### Return Value

The contour object at the specified index path.

## Parameters

- `indexPath`: The hierarchical index path to the contour.

## See Also

- [var contourCount: Int](vncontoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](vncontoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [VNContour]](vncontoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
- [var topLevelContourCount: Int](vncontoursobservation/toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: Int) throws -> VNContour](vncontoursobservation/contour(at:)-9on0y.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [class VNContour](vncontour.md)
  A class that represents a detected contour in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation/contour(at:)-52odo)*