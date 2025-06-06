# encode(to:sourceTexture:previousTexture:destinationTexture:motionVectorTexture:depthTexture:)

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
func encode(to commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthTexture: (any MTLTexture)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporalaa/3143584-encode)*