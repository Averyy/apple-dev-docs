# MPSImageGuidedFilter

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that performs edge-aware filtering on an image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSImageGuidedFilter : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageguidedfilter/2951903-init.md)
- [init(device: any MTLDevice, kernelDiameter: Int)](mpsimageguidedfilter/2951910-init.md)
### Instance Properties
- [var epsilon: Float](mpsimageguidedfilter/2951908-epsilon.md)
- [var kernelDiameter: Int](mpsimageguidedfilter/2951909-kerneldiameter.md)
- [var reconstructOffset: Float](mpsimageguidedfilter/2953079-reconstructoffset.md)
- [var reconstructScale: Float](mpsimageguidedfilter/2953078-reconstructscale.md)
### Instance Methods
- [func encodeReconstruction(commandBuffer: any MTLCommandBuffer, guidance: any MTLTexture, coefficientsA: any MTLTexture, coefficientsB: any MTLTexture, destination: any MTLTexture)](mpsimageguidedfilter/3516398-encodereconstruction.md)
- [func encodeReconstruction(to: any MTLCommandBuffer, guidanceTexture: any MTLTexture, coefficientsTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsimageguidedfilter/2951906-encodereconstruction.md)
- [func encodeRegression(commandBuffer: any MTLCommandBuffer, source: any MTLTexture, guidance: any MTLTexture, weights: (any MTLTexture)?, destinationCoefficientsA: any MTLTexture, destinationCoefficientsB: any MTLTexture)](mpsimageguidedfilter/3516399-encoderegression.md)
- [func encodeRegression(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, guidanceTexture: any MTLTexture, weightsTexture: (any MTLTexture)?, destinationCoefficientsTexture: any MTLTexture)](mpsimageguidedfilter/2951907-encoderegression.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageguidedfilter)*