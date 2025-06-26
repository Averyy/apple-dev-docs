# MPSSVGF

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSSVGF
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpssvgf/init(coder:device:).md)
- [init(device: any MTLDevice)](mpssvgf/init(device:).md)
### Instance Properties
- [var bilateralFilterRadius: Int](mpssvgf/bilateralfilterradius.md)
- [var bilateralFilterSigma: Float](mpssvgf/bilateralfiltersigma.md)
- [var channelCount: Int](mpssvgf/channelcount.md)
- [var channelCount2: Int](mpssvgf/channelcount2.md)
- [var depthWeight: Float](mpssvgf/depthweight.md)
- [var luminanceWeight: Float](mpssvgf/luminanceweight.md)
- [var minimumFramesForVarianceEstimation: Int](mpssvgf/minimumframesforvarianceestimation.md)
- [var normalWeight: Float](mpssvgf/normalweight.md)
- [var reprojectionThreshold: Float](mpssvgf/reprojectionthreshold.md)
- [var temporalReprojectionBlendFactor: Float](mpssvgf/temporalreprojectionblendfactor.md)
- [var temporalWeighting: MPSTemporalWeighting](mpssvgf/temporalweighting.md)
- [var varianceEstimationRadius: Int](mpssvgf/varianceestimationradius.md)
- [var varianceEstimationSigma: Float](mpssvgf/varianceestimationsigma.md)
- [var variancePrefilterRadius: Int](mpssvgf/varianceprefilterradius.md)
- [var variancePrefilterSigma: Float](mpssvgf/varianceprefiltersigma.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpssvgf/copy(with:device:).md)
- [func encode(with: NSCoder)](mpssvgf/encode(with:).md)
- [func encodeBilateralFilter(to: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, depthNormalTexture: any MTLTexture)](mpssvgf/encodebilateralfilter(to:stepdistance:sourcetexture:destinationtexture:depthnormaltexture:).md)
- [func encodeBilateralFilter(to: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, depthNormalTexture: any MTLTexture)](mpssvgf/encodebilateralfilter(to:stepdistance:sourcetexture:destinationtexture:sourcetexture2:destinationtexture2:depthnormaltexture:).md)
- [func encodeReprojection(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, previousFrameCount: any MTLTexture, destinationFrameCount: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)](mpssvgf/encodereprojection(to:sourcetexture:previoustexture:destinationtexture:previousluminancemomentstexture:destinationluminancemomentstexture:previousframecount:destinationframecount:motionvectortexture:depthnormaltexture:previousdepthnormaltex-3k6zp.md)
- [func encodeReprojection(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, previousTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, previousLuminanceMomentsTexture2: (any MTLTexture)?, destinationLuminanceMomentsTexture2: (any MTLTexture)?, previousFrameCount: any MTLTexture, destinationFrameCount: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)](mpssvgf/encodereprojection(to:sourcetexture:previoustexture:destinationtexture:previousluminancemomentstexture:destinationluminancemomentstexture:sourcetexture2:previoustexture2:destinationtexture2:previousluminancemomentstexture2:destinationlumina-5nbfn.md)
- [func encodeVarianceEstimation(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, frameCount: any MTLTexture, depthNormalTexture: (any MTLTexture)?)](mpssvgf/encodevarianceestimation(to:sourcetexture:luminancemomentstexture:destinationtexture:framecount:depthnormaltexture:).md)
- [func encodeVarianceEstimation(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, luminanceMomentsTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, frameCount: any MTLTexture, depthNormalTexture: (any MTLTexture)?)](mpssvgf/encodevarianceestimation(to:sourcetexture:luminancemomentstexture:destinationtexture:sourcetexture2:luminancemomentstexture2:destinationtexture2:framecount:depthnormaltexture:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf)*