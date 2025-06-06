# MPSCNNMultiaryKernel

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
class MPSCNNMultiaryKernel : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnmultiarykernel/3043425-init.md)
- [init(device: any MTLDevice, sourceCount: Int)](mpscnnmultiarykernel/3043426-init.md)
### Instance Properties
- [var clipRect: MTLRegion](mpscnnmultiarykernel/3043412-cliprect.md)
- [var destinationFeatureChannelOffset: Int](mpscnnmultiarykernel/3043413-destinationfeaturechanneloffset.md)
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnmultiarykernel/3043414-destinationimageallocator.md)
- [var isBackwards: Bool](mpscnnmultiarykernel/3043427-isbackwards.md)
- [var isStateModified: Bool](mpscnnmultiarykernel/3043429-isstatemodified.md)
- [var padding: any MPSNNPadding](mpscnnmultiarykernel/3043433-padding.md)
- [var sourceCount: Int](mpscnnmultiarykernel/3043446-sourcecount.md)
### Instance Methods
- [func appendBatchBarrier() -> Bool](mpscnnmultiarykernel/3043411-appendbatchbarrier.md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnmultiarykernel/3043415-destinationimagedescriptor.md)
- [func dilationRateXatIndex(Int) -> Int](mpscnnmultiarykernel/3043416-dilationratexatindex.md)
- [func dilationRateYatIndex(Int) -> Int](mpscnnmultiarykernel/3043417-dilationrateyatindex.md)
- [func edgeMode(at: Int) -> MPSImageEdgeMode](mpscnnmultiarykernel/3043418-edgemode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage](mpscnnmultiarykernel/3043422-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImage: MPSImage)](mpscnnmultiarykernel/3043423-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnmultiarykernel/3043424-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]]) -> [MPSImage]](mpscnnmultiarykernel/3043419-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationImages: [MPSImage])](mpscnnmultiarykernel/3043420-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnmultiarykernel/3043421-encodebatch.md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnmultiarykernel/3043428-isresultstatereusedacrossbatch.md)
- [func kernelHeight(at: Int) -> Int](mpscnnmultiarykernel/3043430-kernelheight.md)
- [func kernelWidth(at: Int) -> Int](mpscnnmultiarykernel/3043431-kernelwidth.md)
- [func offset(at: Int) -> MPSOffset](mpscnnmultiarykernel/3043432-offset.md)
- [func resultState(sourceImages: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnmultiarykernel/3043435-resultstate.md)
- [func resultStateBatch(sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnmultiarykernel/3043434-resultstatebatch.md)
- [func setDilationRateX(Int, at: Int)](mpscnnmultiarykernel/3043436-setdilationratex.md)
- [func setDilationRateY(Int, at: Int)](mpscnnmultiarykernel/3043437-setdilationratey.md)
- [func setEdgeMode(MPSImageEdgeMode, at: Int)](mpscnnmultiarykernel/3043438-setedgemode.md)
- [func setKernelHeight(Int, at: Int)](mpscnnmultiarykernel/3043439-setkernelheight.md)
- [func setKernelWidth(Int, at: Int)](mpscnnmultiarykernel/3043440-setkernelwidth.md)
- [func setOffset(MPSOffset, at: Int)](mpscnnmultiarykernel/3043441-setoffset.md)
- [func setSourceFeatureChannelMaxCount(Int, at: Int)](mpscnnmultiarykernel/3043442-setsourcefeaturechannelmaxcount.md)
- [func setSourceFeatureChannelOffset(Int, at: Int)](mpscnnmultiarykernel/3043443-setsourcefeaturechanneloffset.md)
- [func setStrideInPixelsX(Int, at: Int)](mpscnnmultiarykernel/3043444-setstrideinpixelsx.md)
- [func setStrideInPixelsY(Int, at: Int)](mpscnnmultiarykernel/3043445-setstrideinpixelsy.md)
- [func sourceFeatureChannelMaxCount(at: Int) -> Int](mpscnnmultiarykernel/3043447-sourcefeaturechannelmaxcount.md)
- [func sourceFeatureChannelOffset(at: Int) -> Int](mpscnnmultiarykernel/3043448-sourcefeaturechanneloffset.md)
- [func stride(inPixelsXatIndex: Int) -> Int](mpscnnmultiarykernel/3043449-stride.md)
- [func stride(inPixelsYatIndex: Int) -> Int](mpscnnmultiarykernel/3043450-stride.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnmultiarykernel/3043452-temporaryresultstate.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnmultiarykernel/3043451-temporaryresultstatebatch.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel)*