# VNCircle

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNCircle : NSObject
```

## Topics

### Creating a Circle
- [init(center: VNPoint, radius: Double)](./vncircle/init%28center,radius%29.md)
  Creates a circle with the specified center and radius.
- [convenience init(center: VNPoint, diameter: Double)](./vncircle/init%28center,diameter%29.md)
  Creates a circle with the specified center and diameter.
- [init?(coder: NSCoder)](./vncircle/init%28coder%29.md)
- [class var zero: VNCircle](./vncircle/zero.md)
  A circle object centered at the origin, with a radius of zero.
### Inspecting a Circle
- [var center: VNPoint](./vncircle/center.md)
  The circle’s center point.
- [var diameter: Double](./vncircle/diameter.md)
  The circle’s diameter.
- [var radius: Double](./vncircle/radius.md)
  The circle’s radius.
- [func contains(VNPoint) -> Bool](./vncircle/contains%28_%29.md)
  Determines if this circle, including its boundary, contains the specified point.
- [func contains(VNPoint, inCircumferentialRingOfWidth: Double) -> Bool](./vncircle/contains%28_,incircumferentialringofwidth%29.md)
  Determines if a ring around this circle’s circumference contains the specified point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Common data types
- [class VNVector](./vnvector.md)
  An immutable 2D vector represented by its x-axis and y-axis projections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle)*