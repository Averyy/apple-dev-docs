# value(at:)

**Framework**: Core Image  
**Kind**: method

Returns a value from a specific position in the vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func value(at index: Int) -> CGFloat
```

#### Return Value

The value retrieved from the vector or `0` if the position is undefined.

#### Discussion

The numbering of elements in a vector begins with zero.

## Parameters

- `index`: The position in the vector of the value that you want to retrieve.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/value(at:))*