# MPSSVGF

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
class MPSSVGF : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpssvgf/3143565-init.md)
- [init(device: any MTLDevice)](mpssvgf/3143566-init.md)
### Instance Properties
- [var bilateralFilterRadius: Int](mpssvgf/3143555-bilateralfilterradius.md)
- [var bilateralFilterSigma: Float](mpssvgf/3143556-bilateralfiltersigma.md)
- [var channelCount: Int](mpssvgf/3143557-channelcount.md)
- [var channelCount2: Int](mpssvgf/3143558-channelcount2.md)
- [var depthWeight: Float](mpssvgf/3143560-depthweight.md)
- [var luminanceWeight: Float](mpssvgf/3143567-luminanceweight.md)
- [var minimumFramesForVarianceEstimation: Int](mpssvgf/3143568-minimumframesforvarianceestimati.md)
- [var normalWeight: Float](mpssvgf/3143569-normalweight.md)
- [var reprojectionThreshold: Float](mpssvgf/3143570-reprojectionthreshold.md)
- [var temporalReprojectionBlendFactor: Float](mpssvgf/3143571-temporalreprojectionblendfactor.md)
- [var temporalWeighting: MPSTemporalWeighting](mpssvgf/3143572-temporalweighting.md)
- [var varianceEstimationRadius: Int](mpssvgf/3143573-varianceestimationradius.md)
- [var varianceEstimationSigma: Float](mpssvgf/3143574-varianceestimationsigma.md)
- [var variancePrefilterRadius: Int](mpssvgf/3143575-varianceprefilterradius.md)
- [var variancePrefilterSigma: Float](mpssvgf/3143576-varianceprefiltersigma.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpssvgf/3143559-copy.md)
- [func encode(with: NSCoder)](mpssvgf/3143564-encode.md)
- [func encodeBilateralFilter(to: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, depthNormalTexture: any MTLTexture)](mpssvgf/3242891-encodebilateralfilter.md)
- [func encodeBilateralFilter(to: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, depthNormalTexture: any MTLTexture)](mpssvgf/3143561-encodebilateralfilter.md)
- [func encodeReprojection(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, previousFrameCount: any MTLTexture, destinationFrameCount: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)](mpssvgf/3242892-encodereprojection.md)
- [func encodeReprojection(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, previousTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, previousLuminanceMomentsTexture2: (any MTLTexture)?, destinationLuminanceMomentsTexture2: (any MTLTexture)?, previousFrameCount: any MTLTexture, destinationFrameCount: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)](mpssvgf/3143562-encodereprojection.md)
- [func encodeVarianceEstimation(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, frameCount: any MTLTexture, depthNormalTexture: (any MTLTexture)?)](mpssvgf/3242893-encodevarianceestimation.md)
- [func encodeVarianceEstimation(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, luminanceMomentsTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, frameCount: any MTLTexture, depthNormalTexture: (any MTLTexture)?)](mpssvgf/3143563-encodevarianceestimation.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf)*