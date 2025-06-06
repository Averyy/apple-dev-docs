# MPSAccelerationStructure

**Framework**: Metal Performance Shaders  
**Kind**: cl

The base class for data structures that are built over geometry and used to accelerate ray tracing.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSAccelerationStructure : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsaccelerationstructure/2980765-init.md)
- [init?(coder: NSCoder, group: MPSAccelerationStructureGroup)](mpsaccelerationstructure/2980766-init.md)
- [init(device: any MTLDevice)](mpsaccelerationstructure/2980767-init.md)
- [init(group: MPSAccelerationStructureGroup)](mpsaccelerationstructure/2980768-init.md)
### Instance Properties
- [var boundingBox: MPSAxisAlignedBoundingBox](mpsaccelerationstructure/2980759-boundingbox.md)
- [var group: MPSAccelerationStructureGroup](mpsaccelerationstructure/2980764-group.md)
- [var status: MPSAccelerationStructureStatus](mpsaccelerationstructure/2980771-status.md)
- [var usage: MPSAccelerationStructureUsage](mpsaccelerationstructure/2980772-usage.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsaccelerationstructure/2980760-copy.md)
- [func copy(with: NSZone?, group: MPSAccelerationStructureGroup) -> Self](mpsaccelerationstructure/2980761-copy.md)
- [func encode(with: NSCoder)](mpsaccelerationstructure/2980763-encode.md)
- [func encodeRefit(commandBuffer: any MTLCommandBuffer)](mpsaccelerationstructure/2980762-encoderefit.md)
- [func rebuild()](mpsaccelerationstructure/2980769-rebuild.md)
- [func rebuild(completionHandler: MPSAccelerationStructureCompletionHandler)](mpsaccelerationstructure/2980770-rebuild.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Animating and Denoising a Raytraced Scene](animating_and_denoising_a_raytraced_scene.md)
  Support dynamic scenes and denoising by extending your ray tracer with Metal Performance Shaders.
- [class MPSRayIntersector](mpsrayintersector.md)
  A kernel that performs intersection tests between rays and geometry.
- [class MPSAccelerationStructureGroup](mpsaccelerationstructuregroup.md)
  A group of acceleration structures.
- [class MPSInstanceAccelerationStructure](mpsinstanceaccelerationstructure.md)
  An acceleration structure built over instances of other acceleration structures.
- [class MPSTriangleAccelerationStructure](mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructure)*