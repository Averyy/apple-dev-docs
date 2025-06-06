# MPSNDArrayDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayDescriptor : NSObject
```

## Topics

### Initializers
- [init(dataType: MPSDataType, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>)](mpsndarraydescriptor/3114063-init.md)
- [init(dataType: MPSDataType, shape: [NSNumber])](mpsndarraydescriptor/3143491-init.md)
### Instance Properties
- [var dataType: MPSDataType](mpsndarraydescriptor/3114062-datatype.md)
- [var numberOfDimensions: Int](mpsndarraydescriptor/3114067-numberofdimensions.md)
- [var preferPackedRows: Bool](mpsndarraydescriptor/4423114-preferpackedrows.md)
### Instance Methods
- [func dimensionOrder() -> vector_uchar16](mpsndarraydescriptor/3114065-dimensionorder.md)
- [func getShape() -> [NSNumber]](mpsndarraydescriptor/4423112-getshape.md)
- [func length(ofDimension: Int) -> Int](mpsndarraydescriptor/3114066-length.md)
- [func permute(withDimensionOrder: UnsafeMutablePointer<Int>)](mpsndarraydescriptor/4423113-permute.md)
- [func reshape(withDimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>)](mpsndarraydescriptor/3143492-reshape.md)
- [func reshape(withShape: [NSNumber])](mpsndarraydescriptor/3143493-reshape.md)
- [func sliceDimension(Int, withSubrange: MPSDimensionSlice)](mpsndarraydescriptor/3114069-slicedimension.md)
- [func sliceRange(forDimension: Int) -> MPSDimensionSlice](mpsndarraydescriptor/3114070-slicerange.md)
- [func transposeDimension(Int, withDimension: Int)](mpsndarraydescriptor/3114071-transposedimension.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraydescriptor)*