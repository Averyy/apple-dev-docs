# init(x:y:z:w:)

**Framework**: Core Image  
**Kind**: init

Initializes four positions of a vector with the provided values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)
```

## Parameters

- `x`: The initialization value for the first position.
- `y`: The initialization value for the second position.
- `z`: The initialization value for the third position.
- `w`: The initialization value for the fourth position.

## See Also

- [init(values: UnsafePointer<CGFloat>, count: Int)](civector/init(values:count:).md)
  Initializes a vector with the provided values.
- [convenience init(x: CGFloat)](civector/init(x:).md)
  Initializes the first position of a vector with the provided values.
- [convenience init(x: CGFloat, y: CGFloat)](civector/init(x:y:).md)
  Initializes the first two positions of a vector with the provided values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat)](civector/init(x:y:z:).md)
  Initializes the first three positions of a vector with the provided values.
- [convenience init(string: String)](civector/init(string:).md)
  Initializes a vector with values provided in a string representation.
- [convenience init(cgAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:).md)
  Initializes a vector that is initialized with values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:).md)
  Initializes a vector that is initialized with values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:).md)
  Initializes a vector that is initialized with values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(x:y:z:w:))*