# writeBytes(_:dataLayout:bytesPerColumn:bytesPerRow:bytesPerImage:region:featureChannelInfo:imageIndex:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func writeBytes(_ dataBytes: UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerColumn: Int, bytesPerRow: Int, bytesPerImage: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/3143488-writebytes)*