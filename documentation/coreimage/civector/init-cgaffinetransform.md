# init(cgAffineTransform:)

**Framework**: Core Image  
**Kind**: init

Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(cgAffineTransform t: CGAffineTransform)
```

#### Return Value

 An initialized [`CIVector`](civector.md) object of length 6.

#### Discussion

The `CGAffineTransform` structure’s `a`, `b`, `c`, `c`, `tx` and `ty` values are stored in the vector’s six values.

## Parameters

- `t`: The   structure.

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
- [convenience init(string: String)](civector/init(string:).md)
  Initialize a Core Image vector object with values provided in a string representation.
- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:).md)
  Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:).md)
  Initialize a Core Image vector object with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgaffinetransform:))*