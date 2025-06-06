# CIVector

**Framework**: Core Image  
**Kind**: cl

A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIVector : NSObject
```

## Topics

### Initializing a Vector
- [init(values: UnsafePointer<CGFloat>, count: Int)](civector/1437849-init.md)
  Initializes a vector with the provided values.
- [init(x: CGFloat)](civector/1437657-init.md)
  Initializes the first position of a vector with the provided values.
- [init(x: CGFloat, y: CGFloat)](civector/1437865-init.md)
  Initializes the first two positions of a vector with the provided values.
- [init(x: CGFloat, y: CGFloat, z: CGFloat)](civector/1438056-init.md)
  Initializes the first three positions of a vector with the provided values.
- [init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](civector/1438088-init.md)
  Initializes four positions of a vector with the provided values.
- [init(string: String)](civector/1437938-init.md)
  Initializes a vector with values provided in a string representation.
- [init(cgAffineTransform: CGAffineTransform)](civector/1438102-init.md)
  Initializes a vector that is initialized with values provided by a `CGAffineTransform` structure.
- [init(cgPoint: CGPoint)](civector/1438133-init.md)
  Initializes a vector that is initialized with values provided by a `CGPoint` structure.
- [init(cgRect: CGRect)](civector/1437644-init.md)
  Initializes a vector that is initialized with values provided by a `CGRect` structure.
### Getting Values From a Vector
- [func value(at: Int) -> CGFloat](civector/1438207-value.md)
  Returns a value from a specific position in the vector.
- [var count: Int](civector/1438197-count.md)
  The number of items in the vector.
- [var x: CGFloat](civector/1437738-x.md)
  The value located in the first position in the vector.
- [var y: CGFloat](civector/1437843-y.md)
  The value located in the second position in the vector.
- [var z: CGFloat](civector/1437627-z.md)
  The value located in the third position in the vector.
- [var w: CGFloat](civector/1438058-w.md)
  The value located in the fourth position in the vector.
- [var stringRepresentation: String](civector/1437752-stringrepresentation.md)
  The string representation of the vector.
- [var cgAffineTransformValue: CGAffineTransform](civector/1438249-cgaffinetransformvalue.md)
  The values in the vector represented as an affine transform.
- [var cgPointValue: CGPoint](civector/1437672-cgpointvalue.md)
  The values in the vector as a Core Graphics point structure.
- [var cgRectValue: CGRect](civector/1438108-cgrectvalue.md)
  The values in the vector as a Core Graphics rectangle structure.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CIFilter](cifilter.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The component values defining a color in a specific color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector)*