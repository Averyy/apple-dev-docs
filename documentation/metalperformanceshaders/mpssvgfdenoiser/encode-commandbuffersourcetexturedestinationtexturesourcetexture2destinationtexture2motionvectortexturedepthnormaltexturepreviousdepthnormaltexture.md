# encode(commandBuffer:sourceTexture:destinationTexture:sourceTexture2:destinationTexture2:motionVectorTexture:depthNormalTexture:previousDepthNormalTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: AutoreleasingUnsafeMutablePointer<any MTLTexture>, sourceTexture2: (any MTLTexture)?, destinationTexture2: AutoreleasingUnsafeMutablePointer<any MTLTexture>?, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser/encode(commandbuffer:sourcetexture:destinationtexture:sourcetexture2:destinationtexture2:motionvectortexture:depthnormaltexture:previousdepthnormaltexture:))*