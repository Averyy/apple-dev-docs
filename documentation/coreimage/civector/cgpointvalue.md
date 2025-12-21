# cgPointValue

**Framework**: Core Image  
**Kind**: property

Returns the values in the vector as a `CGPoint` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var cgPointValue: CGPoint { get }
```

#### Return Value

 Reading this property returns a `CGPoint` structure from the `X` and `Y` values from the vector.

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
  The value located in the forth position in the vector.
- [var stringRepresentation: String](civector/stringrepresentation.md)
  Returns a formatted string with all the values of a `CIVector`.
- [var cgAffineTransformValue: CGAffineTransform](civector/cgaffinetransformvalue.md)
  Returns the values in the vector as a `CGAffineTransformValue` structure.
- [var cgRectValue: CGRect](civector/cgrectvalue.md)
  Returns the values in the vector as a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/cgpointvalue)*