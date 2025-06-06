# init(requestRevision:topLeft:bottomLeft:bottomRight:topRight:)

**Framework**: Vision  
**Kind**: init

Creates a rectangle observation from its corner points.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(requestRevision: Int, topLeft: CGPoint, bottomLeft: CGPoint, bottomRight: CGPoint, topRight: CGPoint)
```

## Parameters

- `requestRevision`: The rectangle detector revision number. A higher revision indicates more recent iterations of the framework.
- `topLeft`: The upper-left corner point.
- `bottomLeft`: The lower-left corner point.
- `bottomRight`: The lower-right corner point.
- `topRight`: The upper-right corner point.

## See Also

- [convenience init(requestRevision: Int, topLeft: CGPoint, topRight: CGPoint, bottomRight: CGPoint, bottomLeft: CGPoint)](vnrectangleobservation/init(requestrevision:topleft:topright:bottomright:bottomleft:).md)
  Creates a rectangle observation from its corner points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrectangleobservation/init(requestrevision:topleft:bottomleft:bottomright:topright:))*