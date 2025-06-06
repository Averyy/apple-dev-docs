# zero

**Framework**: Vision  
**Kind**: property

A point object that represents the origin.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var zero: VNPoint { get }
```

#### Discussion

The origin point is (0.0, 0.0).

## See Also

- [init(x: Double, y: Double)](vnpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [convenience init(location: CGPoint)](vnpoint/init(location:).md)
  Creates a point object from the specified Core Graphics point.
- [class func apply(VNVector, to: VNPoint) -> VNPoint](vnpoint/apply(_:to:).md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/zero)*