# MPSCNNBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSCNNBinaryKernel : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinarykernel/2865640-init.md)
- [init(device: any MTLDevice)](mpscnnbinarykernel/2865629-init.md)
### Instance Properties
- [var clipRect: MTLRegion](mpscnnbinarykernel/2865641-cliprect.md)
- [var destinationFeatureChannelOffset: Int](mpscnnbinarykernel/2865643-destinationfeaturechanneloffset.md)
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnbinarykernel/2865651-destinationimageallocator.md)
- [var isBackwards: Bool](mpscnnbinarykernel/2865652-isbackwards.md)
- [var padding: any MPSNNPadding](mpscnnbinarykernel/2865630-padding.md)
- [var primaryEdgeMode: MPSImageEdgeMode](mpscnnbinarykernel/2865646-primaryedgemode.md)
- [var primaryOffset: MPSOffset](mpscnnbinarykernel/2865645-primaryoffset.md)
- [var primaryStrideInPixelsX: Int](mpscnnbinarykernel/2865658-primarystrideinpixelsx.md)
- [var primaryStrideInPixelsY: Int](mpscnnbinarykernel/2865656-primarystrideinpixelsy.md)
- [var secondaryEdgeMode: MPSImageEdgeMode](mpscnnbinarykernel/2865631-secondaryedgemode.md)
- [var secondaryOffset: MPSOffset](mpscnnbinarykernel/2865628-secondaryoffset.md)
- [var secondaryStrideInPixelsX: Int](mpscnnbinarykernel/2865649-secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](mpscnnbinarykernel/2865639-secondarystrideinpixelsy.md)
- [var isStateModified: Bool](mpscnnbinarykernel/2942660-isstatemodified.md)
- [var primaryDilationRateX: Int](mpscnnbinarykernel/2942677-primarydilationratex.md)
- [var primaryDilationRateY: Int](mpscnnbinarykernel/2942662-primarydilationratey.md)
- [var primaryKernelHeight: Int](mpscnnbinarykernel/2942648-primarykernelheight.md)
- [var primaryKernelWidth: Int](mpscnnbinarykernel/2942666-primarykernelwidth.md)
- [var primarySourceFeatureChannelMaxCount: Int](mpscnnbinarykernel/2951919-primarysourcefeaturechannelmaxco.md)
- [var primarySourceFeatureChannelOffset: Int](mpscnnbinarykernel/2942656-primarysourcefeaturechanneloffse.md)
- [var secondaryDilationRateX: Int](mpscnnbinarykernel/2942645-secondarydilationratex.md)
- [var secondaryDilationRateY: Int](mpscnnbinarykernel/2942667-secondarydilationratey.md)
- [var secondaryKernelHeight: Int](mpscnnbinarykernel/2942664-secondarykernelheight.md)
- [var secondaryKernelWidth: Int](mpscnnbinarykernel/2942658-secondarykernelwidth.md)
- [var secondarySourceFeatureChannelMaxCount: Int](mpscnnbinarykernel/2951918-secondarysourcefeaturechannelmax.md)
- [var secondarySourceFeatureChannelOffset: Int](mpscnnbinarykernel/2942654-secondarysourcefeaturechanneloff.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage) -> MPSImage](mpscnnbinarykernel/2865632-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpscnnbinarykernel/2865636-encode.md)
- [func appendBatchBarrier() -> Bool](mpscnnbinarykernel/2942642-appendbatchbarrier.md)
- [func batchEncodingStorageSize(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](mpscnnbinarykernel/3237261-batchencodingstoragesize.md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnbinarykernel/2942686-destinationimagedescriptor.md)
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnbinarykernel/2947936-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage]) -> [MPSImage]](mpscnnbinarykernel/2942650-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationImages: [MPSImage])](mpscnnbinarykernel/2942670-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnbinarykernel/2947934-encodebatch.md)
- [func encodingStorageSize(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](mpscnnbinarykernel/3237262-encodingstoragesize.md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnbinarykernel/2942659-isresultstatereusedacrossbatch.md)
- [func resultState(primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnbinarykernel/2947935-resultstate.md)
- [func resultStateBatch(primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnbinarykernel/2947930-resultstatebatch.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnbinarykernel/2947938-temporaryresultstate.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, primaryImage: [MPSImage], secondaryImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnbinarykernel/2947933-temporaryresultstatebatch.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSCNNKernel](mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNGradientKernel](mpscnngradientkernel.md)
  The base class for gradient layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinarykernel)*