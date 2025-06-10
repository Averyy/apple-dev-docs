# cgAffineTransformValue

**Framework**: Core Image  
**Kind**: property

The values in the vector represented as an affine transform.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var cgAffineTransformValue: CGAffineTransform { get }
```

#### Discussion

Reading this property creates a [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) structure from the first six values in the vector.

## See Also

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
- [var cgPointValue: CGPoint](civector/cgpointvalue.md)
  The values in the vector as a Core Graphics point structure.
- [var cgRectValue: CGRect](civector/cgrectvalue.md)
  The values in the vector as a Core Graphics rectangle structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/cgaffinetransformvalue)*