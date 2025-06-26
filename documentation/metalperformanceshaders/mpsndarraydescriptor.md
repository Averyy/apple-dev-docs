# MPSNDArrayDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayDescriptor
```

## Topics

### Initializers
- [convenience init(dataType: MPSDataType, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>)](mpsndarraydescriptor/init(datatype:dimensioncount:dimensionsizes:).md)
- [convenience init(dataType: MPSDataType, shape: [NSNumber])](mpsndarraydescriptor/init(datatype:shape:).md)
### Instance Properties
- [var dataType: MPSDataType](mpsndarraydescriptor/datatype.md)
- [var numberOfDimensions: Int](mpsndarraydescriptor/numberofdimensions.md)
- [var preferPackedRows: Bool](mpsndarraydescriptor/preferpackedrows.md)
### Instance Methods
- [func dimensionOrder() -> vector_uchar16](mpsndarraydescriptor/dimensionorder.md)
- [func getShape() -> [NSNumber]](mpsndarraydescriptor/getshape.md)
- [func length(ofDimension: Int) -> Int](mpsndarraydescriptor/length(ofdimension:).md)
- [func permute(withDimensionOrder: UnsafeMutablePointer<Int>)](mpsndarraydescriptor/permute(withdimensionorder:).md)
- [func reshape(withDimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>)](mpsndarraydescriptor/reshape(withdimensioncount:dimensionsizes:).md)
- [func reshape(withShape: [NSNumber])](mpsndarraydescriptor/reshape(withshape:).md)
- [func sliceDimension(Int, withSubrange: MPSDimensionSlice)](mpsndarraydescriptor/slicedimension(_:withsubrange:).md)
- [func sliceRange(forDimension: Int) -> MPSDimensionSlice](mpsndarraydescriptor/slicerange(fordimension:).md)
- [func transposeDimension(Int, withDimension: Int)](mpsndarraydescriptor/transposedimension(_:withdimension:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraydescriptor)*