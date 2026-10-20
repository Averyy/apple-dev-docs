# childContours

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSArray<VNContour *> * childContours;
```

## See Also

### Accessing Child Contours
- [var childContourCount: Int](./childcontourcount.md)
  The total number of detected child contours.
- [func childContour(at: Int) throws -> VNContour](./childcontour%28at%29.md)
  Retrieves the child contour object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/childcontours)*