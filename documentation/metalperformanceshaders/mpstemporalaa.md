# MPSTemporalAA

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
class MPSTemporalAA : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpstemporalaa/3143586-init.md)
- [init(device: any MTLDevice)](mpstemporalaa/3143587-init.md)
### Instance Properties
- [var blendFactor: Float](mpstemporalaa/3143582-blendfactor.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpstemporalaa/3143583-copy.md)
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthTexture: (any MTLTexture)?)](mpstemporalaa/3143584-encode.md)
- [func encode(with: NSCoder)](mpstemporalaa/3143585-encode.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporalaa)*