# MPSDataLayout

**Framework**: Metal Performance Shaders  
**Kind**: enum

Options that define how buffer data is arranged.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSDataLayout : UInt, @unchecked Sendable
```

## Topics

### Enumeration Cases
- [MPSDataLayout.featureChannelsxHeightxWidth](mpsdatalayout/featurechannelsxheightxwidth.md)
- [MPSDataLayout.HeightxWidthxFeatureChannels](mpsdatalayout/heightxwidthxfeaturechannels.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/2867105-readbytes.md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/2867188-readbytes.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/2867055-writebytes.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/2867189-writebytes.md)
- [struct MPSImageReadWriteParams](mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatalayout)*