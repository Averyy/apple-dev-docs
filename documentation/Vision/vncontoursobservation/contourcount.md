# contourCount

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The total number of detected contours.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var contourCount: Int { get }
```

```objc
@property (readonly) NSInteger contourCount;
```

#### Discussion

Use this value to determine the number of indices available for calling [`contour(at:)`](./contour%28at%29-9on0y.md).

## See Also

### Inspecting the Observation
- [var normalizedPath: CGPath](./normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation/contourcount)*