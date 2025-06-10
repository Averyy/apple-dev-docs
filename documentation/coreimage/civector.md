# CIVector

**Framework**: Core Image  
**Kind**: class

A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIVector
```

## Topics

### Initializing a Vector
- [init(values: UnsafePointer<CGFloat>, count: Int)](civector/init(values:count:).md)
  Initializes a vector with the provided values.
- [convenience init(x: CGFloat)](civector/init(x:).md)
  Initializes the first position of a vector with the provided values.
- [convenience init(x: CGFloat, y: CGFloat)](civector/init(x:y:).md)
  Initializes the first two positions of a vector with the provided values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat)](civector/init(x:y:z:).md)
  Initializes the first three positions of a vector with the provided values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](civector/init(x:y:z:w:).md)
  Initializes four positions of a vector with the provided values.
- [convenience init(string: String)](civector/init(string:).md)
  Initializes a vector with values provided in a string representation.
- [convenience init(cgAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:).md)
  Initializes a vector that is initialized with values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:).md)
  Initializes a vector that is initialized with values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:).md)
  Initializes a vector that is initialized with values provided by a `CGRect` structure.
### Getting Values From a Vector
- [func value(at: Int) -> CGFloat](civector/value(at:).md)
  Returns a value from a specific position in the vector.
- [var count: Int](civector/count.md)
  The number of items in the vector.
- [var x: CGFloat](civector/x.md)
  The value located in the first position in the vector.
- [var y: CGFloat](civector/y.md)
  The value located in the second position in the vector.
- [var z: CGFloat](civector/z.md)
  The value located in the third position in the vector.
- [var w: CGFloat](civector/w.md)
  The value located in the fourth position in the vector.
- [var stringRepresentation: String](civector/stringrepresentation.md)
  The string representation of the vector.
- [var cgAffineTransformValue: CGAffineTransform](civector/cgaffinetransformvalue.md)
  The values in the vector represented as an affine transform.
- [var cgPointValue: CGPoint](civector/cgpointvalue.md)
  The values in the vector as a Core Graphics point structure.
- [var cgRectValue: CGRect](civector/cgrectvalue.md)
  The values in the vector as a Core Graphics rectangle structure.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CIFilter](cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The component values defining a color in a specific color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector)*