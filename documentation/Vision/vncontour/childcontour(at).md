# childContour(at:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (VNContour *) childContourAtIndex:(NSUInteger) childContourIndex error:(NSError **) error;
```

## Return Value

The child contour object.

## Parameters

- `childContourIndex`: The child contour index value.

## See Also

### Accessing Child Contours
- [var childContourCount: Int](./childcontourcount.md)
  The total number of detected child contours.
- [var childContours: [VNContour]](./childcontours.md)
  An array of contours that this contour encloses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/childcontour(at:))*