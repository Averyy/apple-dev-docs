# init(location:)

**Framework**: Vision  
**Kind**: init

Creates a point object from the specified Core Graphics point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(location: CGPoint)
```

## Parameters

- `location`: The Core Graphics point.

## See Also

- [init(x: Double, y: Double)](vnpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [class func apply(VNVector, to: VNPoint) -> VNPoint](vnpoint/apply(_:to:).md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.
- [class var zero: VNPoint](vnpoint/zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/init(location:))*