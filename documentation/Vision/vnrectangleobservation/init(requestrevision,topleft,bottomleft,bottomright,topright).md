# init(requestRevision:topLeft:bottomLeft:bottomRight:topRight:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a rectangle observation from its corner points.

**Availability**:
- iOS 13.0+ - Deprecated in 17.0
- iPadOS 13.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.15+ - Deprecated in 14.0
- tvOS 13.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(requestRevision:topLeft:topRight:bottomRight:bottomLeft:)`](./init%28requestrevision,topleft,topright,bottomright,bottomleft%29.md) instead.

## Declaration

```swift
convenience init(requestRevision: Int, topLeft: CGPoint, bottomLeft: CGPoint, bottomRight: CGPoint, topRight: CGPoint)
```

```objc
+ (instancetype) rectangleObservationWithRequestRevision:(NSUInteger) requestRevision topLeft:(CGPoint) topLeft bottomLeft:(CGPoint) bottomLeft bottomRight:(CGPoint) bottomRight topRight:(CGPoint) topRight;
```

## Parameters

- `requestRevision`: The rectangle detector revision number. A higher revision indicates more recent iterations of the framework.
- `topLeft`: The upper-left corner point.
- `bottomLeft`: The lower-left corner point.
- `bottomRight`: The lower-right corner point.
- `topRight`: The upper-right corner point.

## See Also

### Creating an Observation
- [convenience init(requestRevision: Int, topLeft: CGPoint, topRight: CGPoint, bottomRight: CGPoint, bottomLeft: CGPoint)](./init%28requestrevision,topleft,topright,bottomright,bottomleft%29.md)
  Creates a rectangle observation from its corner points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrectangleobservation/init(requestrevision:topleft:bottomleft:bottomright:topright:))*