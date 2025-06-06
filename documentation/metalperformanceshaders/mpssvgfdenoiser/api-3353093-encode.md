# encode(commandBuffer:sourceTexture:motionVectorTexture:depthNormalTexture:previousDepthNormalTexture:)

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
func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?) -> any MTLTexture
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser/3353093-encode)*