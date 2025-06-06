# MPSSVGFDenoiser

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSSVGFDenoiser : NSObject
```

## Topics

### Initializers
- [init(SVGF: MPSSVGF, textureAllocator: any MPSSVGFTextureAllocator)](mpssvgfdenoiser/3242908-init.md)
- [init(device: any MTLDevice)](mpssvgfdenoiser/3353094-init.md)
### Instance Properties
- [var bilateralFilterIterations: Int](mpssvgfdenoiser/3242902-bilateralfilteriterations.md)
- [var svgf: MPSSVGF](mpssvgfdenoiser/3242914-svgf.md)
- [var textureAllocator: any MPSSVGFTextureAllocator](mpssvgfdenoiser/3242915-textureallocator.md)
### Instance Methods
- [func clearTemporalHistory()](mpssvgfdenoiser/3242903-cleartemporalhistory.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: AutoreleasingUnsafeMutablePointer<any MTLTexture>, sourceTexture2: (any MTLTexture)?, destinationTexture2: AutoreleasingUnsafeMutablePointer<any MTLTexture>?, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?)](mpssvgfdenoiser/3353092-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?) -> any MTLTexture](mpssvgfdenoiser/3353093-encode.md)
- [func releaseTemporaryTextures()](mpssvgfdenoiser/3242911-releasetemporarytextures.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser)*