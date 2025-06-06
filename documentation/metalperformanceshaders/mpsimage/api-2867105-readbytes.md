# readBytes(_:dataLayout:bytesPerRow:region:featureChannelInfo:imageIndex:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

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

- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/2867188-readbytes.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/2867055-writebytes.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/2867189-writebytes.md)
- [struct MPSImageReadWriteParams](mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.
- [enum MPSDataLayout](mpsdatalayout.md)
  Options that define how buffer data is arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/2867105-readbytes)*