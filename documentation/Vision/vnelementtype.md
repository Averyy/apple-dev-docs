# VNElementType

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum VNElementType : NSUInteger;
```

## Topics

### Element Types
- [VNElementType.unknown](./vnelementtype/unknown.md)
  The element type isn’t known.
- [VNElementType.float](./vnelementtype/float.md)
  The elements are floating-point numbers.
- [VNElementType.double](./vnelementtype/double.md)
  The elements are double-precision floating-point numbers.
### Creating an Element Type
- [init?(rawValue: UInt)](./vnelementtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining Types of Feature Prints
- [var elementType: VNElementType](./vnfeatureprintobservation/elementtype.md)
  The type of each element in the data.
- [func VNElementTypeSize(VNElementType) -> Int](./vnelementtypesize%28_%29.md)
  Returns the size of a feature print element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnelementtype)*