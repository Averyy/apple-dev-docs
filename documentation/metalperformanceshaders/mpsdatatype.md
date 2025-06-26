# MPSDataType

**Framework**: Metal Performance Shaders  
**Kind**: enum

A value to specify a type of data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSDataType
```

## Topics

### Constants
- [MPSDataType.floatBit](mpsdatatype/floatbit.md)
  A common bit for all floating point data types.
- [MPSDataType.float32](mpsdatatype/float32.md)
  A 32-bit floating point type (single precision).
### Enumeration Cases
- [MPSDataType.invalid](mpsdatatype/invalid.md)
- [MPSDataType.float16](mpsdatatype/float16.md)
- [MPSDataType.int16](mpsdatatype/int16.md)
- [MPSDataType.int8](mpsdatatype/int8.md)
- [MPSDataType.normalizedBit](mpsdatatype/normalizedbit.md)
- [MPSDataType.signedBit](mpsdatatype/signedbit.md)
- [MPSDataType.uInt16](mpsdatatype/uint16.md)
- [MPSDataType.uInt32](mpsdatatype/uint32.md)
- [MPSDataType.uInt8](mpsdatatype/uint8.md)
- [MPSDataType.unorm1](mpsdatatype/unorm1.md)
- [MPSDataType.unorm8](mpsdatatype/unorm8.md)
- [MPSDataType.alternateEncodingBit](mpsdatatype/alternateencodingbit.md)
- [MPSDataType.bFloat16](mpsdatatype/bfloat16.md)
- [MPSDataType.bool](mpsdatatype/bool.md)
- [MPSDataType.complexBit](mpsdatatype/complexbit.md)
- [MPSDataType.complexFloat16](mpsdatatype/complexfloat16.md)
- [MPSDataType.complexFloat32](mpsdatatype/complexfloat32.md)
- [MPSDataType.int32](mpsdatatype/int32.md)
- [MPSDataType.int4](mpsdatatype/int4.md)
- [MPSDataType.int64](mpsdatatype/int64.md)
- [MPSDataType.uInt4](mpsdatatype/uint4.md)
- [MPSDataType.uInt64](mpsdatatype/uint64.md)
- [MPSDataType.int2](mpsdatatype/int2.md)
- [MPSDataType.uInt2](mpsdatatype/uint2.md)
### Type Properties
- [static var intBit: MPSDataType](mpsdatatype/intbit.md)
### Initializers
- [init?(rawValue: UInt32)](mpsdatatype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var rows: Int](mpsmatrixdescriptor/rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrixdescriptor/columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrixdescriptor/datatype.md)
  The type of the values in the matrix.
- [var rowBytes: Int](mpsmatrixdescriptor/rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var matrices: Int](mpsmatrixdescriptor/matrices.md)
- [var matrixBytes: Int](mpsmatrixdescriptor/matrixbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatatype)*