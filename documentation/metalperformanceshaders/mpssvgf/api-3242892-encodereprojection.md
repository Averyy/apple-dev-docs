# encodeReprojection(to:sourceTexture:previousTexture:destinationTexture:previousLuminanceMomentsTexture:destinationLuminanceMomentsTexture:previousFrameCount:destinationFrameCount:motionVectorTexture:depthNormalTexture:previousDepthNormalTexture:)

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
func encodeReprojection(to commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, previousFrameCount previousFrameCountTexture: any MTLTexture, destinationFrameCount destinationFrameCountTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf/3242892-encodereprojection)*