# init(x:y:)

**Framework**: Vision  
**Kind**: init

Creates a point object with the specified coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(x: Double, y: Double)
```

## Parameters

- `x`: The x-coordinate value.
- `y`: The y-coordinate value.

## See Also

- [convenience init(location: CGPoint)](vnpoint/init(location:).md)
  Creates a point object from the specified Core Graphics point.
- [class func apply(VNVector, to: VNPoint) -> VNPoint](vnpoint/apply(_:to:).md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.
- [class var zero: VNPoint](vnpoint/zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/init(x:y:))*