# readBytes(_:dataLayout:bytesPerRow:bytesPerImage:region:featureChannelInfo:imageIndex:)

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
func readBytes(_ dataBytes: UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, bytesPerImage: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/2951914-readbytes)*