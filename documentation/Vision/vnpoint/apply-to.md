# apply(_:to:)

**Framework**: Vision  
**Kind**: method

Creates a point object that’s shifted by the X and Y offsets of the specified vector.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func apply(_ vector: VNVector, to point: VNPoint) -> VNPoint
```

## Parameters

- `vector`: The vector to apply to offset the point.
- `point`: The point to translate by the vector’s X and Y offsets.

## See Also

- [init(x: Double, y: Double)](vnpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [convenience init(location: CGPoint)](vnpoint/init(location:).md)
  Creates a point object from the specified Core Graphics point.
- [class var zero: VNPoint](vnpoint/zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/apply(_:to:))*