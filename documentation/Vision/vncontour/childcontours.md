# childContours

**Framework**: Vision  
**Kind**: property

An array of contours that this contour encloses.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var childContours: [VNContour] { get }
```

## See Also

- [var childContourCount: Int](vncontour/childcontourcount.md)
  The total number of detected child contours.
- [func childContour(at: Int) throws -> VNContour](vncontour/childcontour(at:).md)
  Retrieves the child contour object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/childcontours)*