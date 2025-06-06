# VNCircle

**Framework**: Vision  
**Kind**: class

An immutable 2D circle represented by its center point and radius.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNCircle
```

## Topics

### Creating a Circle
- [init(center: VNPoint, radius: Double)](vncircle/init(center:radius:).md)
  Creates a circle with the specified center and radius.
- [convenience init(center: VNPoint, diameter: Double)](vncircle/init(center:diameter:).md)
  Creates a circle with the specified center and diameter.
- [class var zero: VNCircle](vncircle/zero.md)
  A circle object centered at the origin, with a radius of zero.
### Inspecting a Circle
- [var center: VNPoint](vncircle/center.md)
  The circle’s center point.
- [var diameter: Double](vncircle/diameter.md)
  The circle’s diameter.
- [var radius: Double](vncircle/radius.md)
  The circle’s radius.
- [func contains(VNPoint) -> Bool](vncircle/contains(_:).md)
  Determines if this circle, including its boundary, contains the specified point.
- [func contains(VNPoint, inCircumferentialRingOfWidth: Double) -> Bool](vncircle/contains(_:incircumferentialringofwidth:).md)
  Determines if a ring around this circle’s circumference contains the specified point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class VNVector](vnvector.md)
  An immutable 2D vector represented by its x-axis and y-axis projections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle)*