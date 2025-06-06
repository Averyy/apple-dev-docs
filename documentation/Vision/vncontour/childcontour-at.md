# childContour(at:)

**Framework**: Vision  
**Kind**: method

Retrieves the child contour object at the specified index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func childContour(at childContourIndex: Int) throws -> VNContour
```

#### Return Value

The child contour object.

## Parameters

- `childContourIndex`: The child contour index value.

## See Also

- [var childContourCount: Int](vncontour/childcontourcount.md)
  The total number of detected child contours.
- [var childContours: [VNContour]](vncontour/childcontours.md)
  An array of contours that this contour encloses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/childcontour(at:))*