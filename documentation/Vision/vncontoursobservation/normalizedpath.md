# normalizedPath

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The detected contours as a path object in normalized coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var normalizedPath: CGPath { get }
```

```objc
@property (readonly) CGPathRef normalizedPath;
```

## See Also

### Inspecting the Observation
- [var contourCount: Int](./contourcount.md)
  The total number of detected contours.
- [var topLevelContours: [VNContour]](./toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
- [var topLevelContourCount: Int](./toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: Int) throws -> VNContour](./contour%28at%29-9on0y.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func contour(at: IndexPath) throws -> VNContour](./contour%28at%29-52odo.md)
  Retrieves the contour object at the specified index path.
- [class VNContour](../vncontour.md)
  A class that represents a detected contour in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation/normalizedpath)*