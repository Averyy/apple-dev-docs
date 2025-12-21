# init(string:)

**Framework**: Core Image  
**Kind**: init

Initialize a Core Image vector object with values provided in a string representation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(string representation: String)
```

#### Return Value

 An initialized [`CIVector`](civector.md) object.

## Parameters

- `representation`: A string that is in one of the formats returned by the   method.

## See Also

- [init(values: UnsafePointer<CGFloat>, count: Int)](civector/init(values:count:).md)
  Initialize a Core Image vector object with the specified the values.
- [convenience init(x: CGFloat)](civector/init(x:).md)
  Initialize a Core Image vector object with one value.
- [convenience init(x: CGFloat, y: CGFloat)](civector/init(x:y:).md)
  Initialize a Core Image vector object with two values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat)](civector/init(x:y:z:).md)
  Initialize a Core Image vector object with three values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](civector/init(x:y:z:w:).md)
  Initialize a Core Image vector object with four values.
- [convenience init(cgAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:).md)
  Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:).md)
  Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:).md)
  Initialize a Core Image vector object with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(string:))*