# MPSNDArray

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
class MPSNDArray : NSObject
```

## Topics

### Initializers
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSNDArrayDescriptor)](mpsndarray/4391636-init.md)
- [init(device: any MTLDevice, descriptor: MPSNDArrayDescriptor)](mpsndarray/3114049-init.md)
- [init(device: any MTLDevice, scalar: Double)](mpsndarray/3114051-init.md)
### Instance Properties
- [var dataType: MPSDataType](mpsndarray/3114041-datatype.md)
- [var dataTypeSize: Int](mpsndarray/3114042-datatypesize.md)
- [var device: any MTLDevice](mpsndarray/3114045-device.md)
- [var label: String?](mpsndarray/3114052-label.md)
- [var numberOfDimensions: Int](mpsndarray/3114055-numberofdimensions.md)
- [var parent: MPSNDArray?](mpsndarray/3114056-parent.md)
### Instance Methods
- [func arrayView(with: MPSNDArrayDescriptor) -> MPSNDArray?](mpsndarray/4438553-arrayview.md)
- [func arrayView(with: any MTLCommandBuffer, descriptor: MPSNDArrayDescriptor, aliasing: MPSAliasingStrategy) -> MPSNDArray?](mpsndarray/3114040-arrayview.md)
- [func arrayView(withDimensionCount: Int, dimensionSizes: UnsafePointer<Int>, strides: UnsafePointer<Int>) -> MPSNDArray?](mpsndarray/4408693-arrayview.md)
- [func arrayView(withShape: [NSNumber]?, strides: [NSNumber]) -> MPSNDArray?](mpsndarray/4408694-arrayview.md)
- [func descriptor() -> MPSNDArrayDescriptor](mpsndarray/3114044-descriptor.md)
- [func exportData(with: any MTLCommandBuffer, to: any MTLBuffer, destinationDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)](mpsndarray/3131729-exportdata.md)
- [func exportData(with: any MTLCommandBuffer, to: [MPSImage], offset: MPSImageCoordinate)](mpsndarray/3152526-exportdata.md)
- [func importData(with: any MTLCommandBuffer, from: [MPSImage], offset: MPSImageCoordinate)](mpsndarray/3152527-importdata.md)
- [func importData(with: any MTLCommandBuffer, from: any MTLBuffer, sourceDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)](mpsndarray/3131730-importdata.md)
- [func length(ofDimension: Int) -> Int](mpsndarray/3114053-length.md)
- [func readBytes(UnsafeMutableRawPointer, strideBytes: UnsafeMutablePointer<Int>?)](mpsndarray/3114057-readbytes.md)
- [func resourceSize() -> Int](mpsndarray/3114058-resourcesize.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsndarray/3114059-synchronize.md)
- [func userBuffer() -> (any MTLBuffer)?](mpsndarray/4408695-userbuffer.md)
- [func writeBytes(UnsafeMutableRawPointer, strideBytes: UnsafeMutablePointer<Int>?)](mpsndarray/3114060-writebytes.md)
### Type Methods
- [class func defaultAllocator() -> any MPSNDArrayAllocator](mpsndarray/3131728-defaultallocator.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray)*