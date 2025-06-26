# MPSNDArrayMultiaryBase

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
class MPSNDArrayMultiaryBase
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraymultiarybase/init(coder:device:).md)
- [init(device: any MTLDevice, sourceCount: Int)](mpsndarraymultiarybase/init(device:sourcecount:).md)
### Instance Properties
- [var destinationArrayAllocator: any MPSNDArrayAllocator](mpsndarraymultiarybase/destinationarrayallocator.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsndarraymultiarybase/copy(with:device:).md)
- [func destinationArrayDescriptor(forSourceArrays: [MPSNDArray], sourceState: MPSState?) -> MPSNDArrayDescriptor](mpsndarraymultiarybase/destinationarraydescriptor(forsourcearrays:sourcestate:).md)
- [func dilationRates(forSourceIndex: Int) -> MPSNDArraySizes](mpsndarraymultiarybase/dilationrates(forsourceindex:).md)
- [func edgeMode(atSourceIndex: Int) -> MPSImageEdgeMode](mpsndarraymultiarybase/edgemode(atsourceindex:).md)
- [func encode(with: NSCoder)](mpsndarraymultiarybase/encode(with:).md)
- [func kernelSizes(forSourceIndex: Int) -> MPSNDArraySizes](mpsndarraymultiarybase/kernelsizes(forsourceindex:).md)
- [func offsets(atSourceIndex: Int) -> MPSNDArrayOffsets](mpsndarraymultiarybase/offsets(atsourceindex:).md)
- [func resultState(forSourceArrays: [MPSNDArray], sourceStates: [MPSState]?, destinationArray: MPSNDArray) -> MPSState?](mpsndarraymultiarybase/resultstate(forsourcearrays:sourcestates:destinationarray:).md)
- [func strides(forSourceIndex: Int) -> MPSNDArrayOffsets](mpsndarraymultiarybase/strides(forsourceindex:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)
- [MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarybase)*