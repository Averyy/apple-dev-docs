# calculateArea(_:for:orientedArea:)

**Framework**: Vision  
**Kind**: method

Calculates the area for the specified contour.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func calculateArea(_ area: UnsafeMutablePointer<Double>, for contour: VNContour, orientedArea: Bool) throws
```

#### Discussion

Attempting to calculate the area for a contour containing random points, or with self-crossing edges, produces undefined results.

## Parameters

- `area`: The output parameter to populate with the calculated contour area.
- `contour`: The contour object for which to calculate the area.
- `orientedArea`: A Boolean value that indicates whether to calculate the signed area (positive for counterclockwise-oriented contours and negative for clockwise-oriented contours). If you specify  , the returned area is always positive.

## See Also

- [class func calculatePerimeter(UnsafeMutablePointer<Double>, for: VNContour) throws](vngeometryutils/calculateperimeter(_:for:).md)
  Calculates the perimeter of a closed contour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeometryutils/calculatearea(_:for:orientedarea:))*