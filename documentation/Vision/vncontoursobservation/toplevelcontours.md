# topLevelContours

**Framework**: Vision  
**Kind**: property

An array of contours that don’t have another contour enclosing them.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var topLevelContours: [VNContour] { get }
```

#### Discussion

This array constitutes the top of the contour hierarchy. You can iterate over each [`VNContour`](vncontour.md) instance to determine its children.

## See Also

- [var contourCount: Int](vncontoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](vncontoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContourCount: Int](vncontoursobservation/toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: Int) throws -> VNContour](vncontoursobservation/contour(at:)-9on0y.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func contour(at: IndexPath) throws -> VNContour](vncontoursobservation/contour(at:)-52odo.md)
  Retrieves the contour object at the specified index path.
- [class VNContour](vncontour.md)
  A class that represents a detected contour in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation/toplevelcontours)*