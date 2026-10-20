# childContourCount

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The total number of detected child contours.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var childContourCount: Int { get }
```

```objc
@property (readonly) NSInteger childContourCount;
```

## See Also

### Accessing Child Contours
- [var childContours: [VNContour]](./childcontours.md)
  An array of contours that this contour encloses.
- [func childContour(at: Int) throws -> VNContour](./childcontour%28at%29.md)
  Retrieves the child contour object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/childcontourcount)*