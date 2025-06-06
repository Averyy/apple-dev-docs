# MPSImageEDLines

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
class MPSImageEDLines : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageedlines/3618920-init.md)
- [init(device: any MTLDevice, gaussianSigma: Float, minLineLength: UInt16, maxLines: Int, detailRatio: UInt16, gradientThreshold: Float, lineErrorThreshold: Float, mergeLocalityThreshold: Float)](mpsimageedlines/3618921-init.md)
### Instance Properties
- [var clipRectSource: MTLRegion](mpsimageedlines/3618915-cliprectsource.md)
- [var detailRatio: UInt16](mpsimageedlines/3618916-detailratio.md)
- [var gaussianSigma: Float](mpsimageedlines/3618918-gaussiansigma.md)
- [var gradientThreshold: Float](mpsimageedlines/3618919-gradientthreshold.md)
- [var lineErrorThreshold: Float](mpsimageedlines/3618922-lineerrorthreshold.md)
- [var maxLines: Int](mpsimageedlines/3618923-maxlines.md)
- [var mergeLocalityThreshold: Float](mpsimageedlines/3618924-mergelocalitythreshold.md)
- [var minLineLength: UInt16](mpsimageedlines/3618925-minlinelength.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: (any MTLTexture)?, endpointBuffer: any MTLBuffer, endpointOffset: Int)](mpsimageedlines/3618917-encode.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedlines)*