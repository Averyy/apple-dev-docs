# zero

**Framework**: Vision  
**Kind**: property  
**Role**: Type Property

A point object that represents the origin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
static var zero: NormalizedPoint { get }
```

## See Also

### Creating a normalized point
- [init(x: CGFloat, y: CGFloat)](./init%28x,y%29.md)
  Creates a point object with the specified coordinates.
- [init(normalizedPoint: CGPoint)](./init%28normalizedpoint%29.md)
  Creates a point object from the specified Core Graphics point.
- [init(imagePoint: CGPoint, in: CGSize)](./init%28imagepoint,in%29.md)
  Creates a normalized point from a point in an image coordinate space.
- [init(imagePoint: CGPoint, in: CGSize, normalizedTo: NormalizedRect)](./init%28imagepoint,in,normalizedto%29.md)
  Creates a point normalized to a region of interest within an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint/zero)*