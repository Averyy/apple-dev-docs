# MPSTemporalAA

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
class MPSTemporalAA
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpstemporalaa/init(coder:device:).md)
- [init(device: any MTLDevice)](mpstemporalaa/init(device:).md)
### Instance Properties
- [var blendFactor: Float](mpstemporalaa/blendfactor.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpstemporalaa/copy(with:device:).md)
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthTexture: (any MTLTexture)?)](mpstemporalaa/encode(to:sourcetexture:previoustexture:destinationtexture:motionvectortexture:depthtexture:).md)
- [func encode(with: NSCoder)](mpstemporalaa/encode(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporalaa)*