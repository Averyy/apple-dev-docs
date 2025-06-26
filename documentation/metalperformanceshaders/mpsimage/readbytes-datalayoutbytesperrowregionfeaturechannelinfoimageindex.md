# readBytes(_:dataLayout:bytesPerRow:region:featureChannelInfo:imageIndex:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func readBytes(_ dataBytes: UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)
```

## See Also

- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/readbytes(_:datalayout:imageindex:).md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/writebytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:).md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/writebytes(_:datalayout:imageindex:).md)
- [struct MPSImageReadWriteParams](mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.
- [enum MPSDataLayout](mpsdatalayout.md)
  Options that define how buffer data is arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/readbytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:))*