# MPSNDArrayMultiaryBase

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
class MPSNDArrayMultiaryBase : MPSKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraymultiarybase/3131740-init.md)
- [init(device: any MTLDevice, sourceCount: Int)](mpsndarraymultiarybase/3131741-init.md)
### Instance Properties
- [var destinationArrayAllocator: any MPSNDArrayAllocator](mpsndarraymultiarybase/3131735-destinationarrayallocator.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsndarraymultiarybase/3131734-copy.md)
- [func destinationArrayDescriptor(forSourceArrays: [MPSNDArray], sourceState: MPSState?) -> MPSNDArrayDescriptor](mpsndarraymultiarybase/3131736-destinationarraydescriptor.md)
- [func dilationRates(forSourceIndex: Int) -> MPSNDArraySizes](mpsndarraymultiarybase/3131737-dilationrates.md)
- [func edgeMode(atSourceIndex: Int) -> MPSImageEdgeMode](mpsndarraymultiarybase/3131738-edgemode.md)
- [func encode(with: NSCoder)](mpsndarraymultiarybase/3131739-encode.md)
- [func kernelSizes(forSourceIndex: Int) -> MPSNDArraySizes](mpsndarraymultiarybase/3131742-kernelsizes.md)
- [func offsets(atSourceIndex: Int) -> MPSNDArrayOffsets](mpsndarraymultiarybase/3131743-offsets.md)
- [func resultState(forSourceArrays: [MPSNDArray], sourceStates: [MPSState]?, destinationArray: MPSNDArray) -> MPSState?](mpsndarraymultiarybase/3143521-resultstate.md)
- [func strides(forSourceIndex: Int) -> MPSNDArrayOffsets](mpsndarraymultiarybase/3131749-strides.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarybase)*