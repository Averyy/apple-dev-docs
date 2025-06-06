# MPSImageReadWriteParams

**Framework**: Metal Performance Shaders  
**Kind**: struct

Parameters that control reading and writing of a particular set of feature channels.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSImageReadWriteParams
```

## Topics

### Initializers
- [init()](mpsimagereadwriteparams/2867022-init.md)
- [init(featureChannelOffset: Int, numberOfFeatureChannelsToReadWrite: Int)](mpsimagereadwriteparams/2867128-init.md)
### Instance Properties
- [var featureChannelOffset: Int](mpsimagereadwriteparams/2867064-featurechanneloffset.md)
- [var numberOfFeatureChannelsToReadWrite: Int](mpsimagereadwriteparams/2867173-numberoffeaturechannelstoreadwri.md)

## See Also

- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/2867105-readbytes.md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/2867188-readbytes.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/2867055-writebytes.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/2867189-writebytes.md)
- [enum MPSDataLayout](mpsdatalayout.md)
  Options that define how buffer data is arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagereadwriteparams)*