# MPSImageReduceUnary

**Framework**: Metal Performance Shaders  
**Kind**: class

The base class for reduction filters that take a single source as input.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSImageReduceUnary
```

## Topics

### Instance Properties
- [var clipRectSource: MTLRegion](mpsimagereduceunary/cliprectsource.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Inherited By
- [MPSImageReduceColumnMax](mpsimagereducecolumnmax.md)
- [MPSImageReduceColumnMean](mpsimagereducecolumnmean.md)
- [MPSImageReduceColumnMin](mpsimagereducecolumnmin.md)
- [MPSImageReduceColumnSum](mpsimagereducecolumnsum.md)
- [MPSImageReduceRowMax](mpsimagereducerowmax.md)
- [MPSImageReduceRowMean](mpsimagereducerowmean.md)
- [MPSImageReduceRowMin](mpsimagereducerowmin.md)
- [MPSImageReduceRowSum](mpsimagereducerowsum.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSImageReduceRowMax](mpsimagereducerowmax.md)
  A filter that returns the maximum value for each row in an image.
- [class MPSImageReduceRowMin](mpsimagereducerowmin.md)
  A filter that returns the minimum value for each row in an image.
- [class MPSImageReduceRowSum](mpsimagereducerowsum.md)
  A filter that returns the sum of all values for a row in an image.
- [class MPSImageReduceRowMean](mpsimagereducerowmean.md)
  A filter that returns the mean value for each row in an image.
- [class MPSImageReduceColumnMax](mpsimagereducecolumnmax.md)
  A filter that returns the maximum value for each column in an image.
- [class MPSImageReduceColumnMin](mpsimagereducecolumnmin.md)
  A filter that returns the minimum value for each column in an image.
- [class MPSImageReduceColumnSum](mpsimagereducecolumnsum.md)
  A filter that returns the sum of all values for a column in an image.
- [class MPSImageReduceColumnMean](mpsimagereducecolumnmean.md)
  A filter that returns the mean value for each column in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagereduceunary)*