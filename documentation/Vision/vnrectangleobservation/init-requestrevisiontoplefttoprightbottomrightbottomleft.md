# init(requestRevision:topLeft:topRight:bottomRight:bottomLeft:)

**Framework**: Vision  
**Kind**: init

Creates a rectangle observation from its corner points.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(requestRevision: Int, topLeft: CGPoint, topRight: CGPoint, bottomRight: CGPoint, bottomLeft: CGPoint)
```

## Parameters

- `requestRevision`: The rectangle detector revision number. A higher revision indicates more recent iterations of the framework.
- `topLeft`: The upper-left corner point.
- `topRight`: The upper-right corner point.
- `bottomRight`: The lower-right corner point.
- `bottomLeft`: The lower-left corner point.

## See Also

- [convenience init(requestRevision: Int, topLeft: CGPoint, bottomLeft: CGPoint, bottomRight: CGPoint, topRight: CGPoint)](vnrectangleobservation/init(requestrevision:topleft:bottomleft:bottomright:topright:).md)
  Creates a rectangle observation from its corner points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrectangleobservation/init(requestrevision:topleft:topright:bottomright:bottomleft:))*