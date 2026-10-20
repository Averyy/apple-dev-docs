# calculatePerimeter(_:for:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Calculates the perimeter of a closed contour.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func calculatePerimeter(_ perimeter: UnsafeMutablePointer<Double>, for contour: VNContour) throws
```

```objc
+ (BOOL) calculatePerimeter:(double *) perimeter forContour:(VNContour *) contour error:(NSError **) error;
```

## Parameters

- `perimeter`: The output parameter to populate with the calculated contour perimeter.
- `contour`: The contour object for which to calculate the perimeter.

## See Also

### Calculating Area and Perimeter
- [class func calculateArea(UnsafeMutablePointer<Double>, for: VNContour, orientedArea: Bool) throws](./calculatearea%28_,for,orientedarea%29.md)
  Calculates the area for the specified contour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeometryutils/calculateperimeter(_:for:))*