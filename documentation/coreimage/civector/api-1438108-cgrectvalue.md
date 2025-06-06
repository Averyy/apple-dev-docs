# cgRectValue

**Framework**: Core Image  
**Kind**: instp

The values in the vector as a Core Graphics rectangle structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var cgRectValue: CGRect { get }
```

#### Discussion

Reading this property creates a [`CGRect`](https://developer.apple.com/documentation/corefoundation/cgrect) structure whose origin is the [`x`](civector/1437738-x.md) and [`y`](civector/1437843-y.md) values in the vector and whose size is the [`z`](civector/1437627-z.md) and [`w`](civector/1438058-w.md) values in the vector.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)*