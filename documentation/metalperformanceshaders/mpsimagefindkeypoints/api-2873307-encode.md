# encode(to:sourceTexture:regions:numberOfRegions:keypointCount:keypointCountBufferOffset:keypointDataBuffer:keypointDataBufferOffset:)

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
func encode(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, regions: UnsafePointer<MTLRegion>, numberOfRegions: Int, keypointCount keypointCountBuffer: any MTLBuffer, keypointCountBufferOffset: Int, keypointDataBuffer: any MTLBuffer, keypointDataBufferOffset: Int)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefindkeypoints/2873307-encode)*