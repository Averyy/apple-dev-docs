# VNElementType

**Framework**: Vision  
**Kind**: enum

An enumeration of the type of element in feature print data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum VNElementType
```

## Topics

### Element Types
- [VNElementType.unknown](vnelementtype/unknown.md)
  The element type isn’t known.
- [VNElementType.float](vnelementtype/float.md)
  The elements are floating-point numbers.
- [VNElementType.double](vnelementtype/double.md)
  The elements are double-precision floating-point numbers.
### Creating an Element Type
- [init?(rawValue: UInt)](vnelementtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var elementType: VNElementType](vnfeatureprintobservation/elementtype.md)
  The type of each element in the data.
- [func VNElementTypeSize(VNElementType) -> Int](vnelementtypesize(_:).md)
  Returns the size of a feature print element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnelementtype)*