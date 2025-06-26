# MPSCNNBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

A convolution neural network kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinarykernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpscnnbinarykernel/init(device:).md)
### Instance Properties
- [var clipRect: MTLRegion](mpscnnbinarykernel/cliprect.md)
- [var destinationFeatureChannelOffset: Int](mpscnnbinarykernel/destinationfeaturechanneloffset.md)
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnbinarykernel/destinationimageallocator.md)
- [var isBackwards: Bool](mpscnnbinarykernel/isbackwards.md)
- [var padding: any MPSNNPadding](mpscnnbinarykernel/padding.md)
- [var primaryEdgeMode: MPSImageEdgeMode](mpscnnbinarykernel/primaryedgemode.md)
- [var primaryOffset: MPSOffset](mpscnnbinarykernel/primaryoffset.md)
- [var primaryStrideInPixelsX: Int](mpscnnbinarykernel/primarystrideinpixelsx.md)
- [var primaryStrideInPixelsY: Int](mpscnnbinarykernel/primarystrideinpixelsy.md)
- [var secondaryEdgeMode: MPSImageEdgeMode](mpscnnbinarykernel/secondaryedgemode.md)
- [var secondaryOffset: MPSOffset](mpscnnbinarykernel/secondaryoffset.md)
- [var secondaryStrideInPixelsX: Int](mpscnnbinarykernel/secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](mpscnnbinarykernel/secondarystrideinpixelsy.md)
- [var isStateModified: Bool](mpscnnbinarykernel/isstatemodified.md)
- [var primaryDilationRateX: Int](mpscnnbinarykernel/primarydilationratex.md)
- [var primaryDilationRateY: Int](mpscnnbinarykernel/primarydilationratey.md)
- [var primaryKernelHeight: Int](mpscnnbinarykernel/primarykernelheight.md)
- [var primaryKernelWidth: Int](mpscnnbinarykernel/primarykernelwidth.md)
- [var primarySourceFeatureChannelMaxCount: Int](mpscnnbinarykernel/primarysourcefeaturechannelmaxcount.md)
- [var primarySourceFeatureChannelOffset: Int](mpscnnbinarykernel/primarysourcefeaturechanneloffset.md)
- [var secondaryDilationRateX: Int](mpscnnbinarykernel/secondarydilationratex.md)
- [var secondaryDilationRateY: Int](mpscnnbinarykernel/secondarydilationratey.md)
- [var secondaryKernelHeight: Int](mpscnnbinarykernel/secondarykernelheight.md)
- [var secondaryKernelWidth: Int](mpscnnbinarykernel/secondarykernelwidth.md)
- [var secondarySourceFeatureChannelMaxCount: Int](mpscnnbinarykernel/secondarysourcefeaturechannelmaxcount.md)
- [var secondarySourceFeatureChannelOffset: Int](mpscnnbinarykernel/secondarysourcefeaturechanneloffset.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage) -> MPSImage](mpscnnbinarykernel/encode(commandbuffer:primaryimage:secondaryimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpscnnbinarykernel/encode(commandbuffer:primaryimage:secondaryimage:destinationimage:).md)
- [func appendBatchBarrier() -> Bool](mpscnnbinarykernel/appendbatchbarrier.md)
- [func batchEncodingStorageSize(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](mpscnnbinarykernel/batchencodingstoragesize(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnbinarykernel/destinationimagedescriptor(forsourceimages:sourcestates:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnbinarykernel/encode(commandbuffer:primaryimage:secondaryimage:destinationstate:destinationstateistemporary:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage]) -> [MPSImage]](mpscnnbinarykernel/encodebatch(commandbuffer:primaryimages:secondaryimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationImages: [MPSImage])](mpscnnbinarykernel/encodebatch(commandbuffer:primaryimages:secondaryimages:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnbinarykernel/encodebatch(commandbuffer:primaryimages:secondaryimages:destinationstates:destinationstateistemporary:).md)
- [func encodingStorageSize(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](mpscnnbinarykernel/encodingstoragesize(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnbinarykernel/isresultstatereusedacrossbatch.md)
- [func resultState(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnbinarykernel/resultstate(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func resultStateBatch(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnbinarykernel/resultstatebatch(primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnbinarykernel/temporaryresultstate(commandbuffer:primaryimage:secondaryimage:sourcestates:destinationimage:).md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnbinarykernel/temporaryresultstatebatch(commandbuffer:primaryimage:secondaryimage:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSCNNArithmetic](mpscnnarithmetic.md)
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
- [MPSNNGridSample](mpsnngridsample.md)
- [MPSNNLossGradient](mpsnnlossgradient.md)
- [MPSNNReduceBinary](mpsnnreducebinary.md)
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

- [class MPSCNNKernel](mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNGradientKernel](mpscnngradientkernel.md)
  The base class for gradient layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinarykernel)*