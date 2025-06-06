# MPSAccelerationStructureGroup

**Framework**: Metal Performance Shaders  
**Kind**: cl

A group of acceleration structures.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSAccelerationStructureGroup : NSObject
```

## Topics

### Initializers
- [init(device: any MTLDevice)](mpsaccelerationstructuregroup/2980784-init.md)
### Instance Properties
- [var device: any MTLDevice](mpsaccelerationstructuregroup/2980783-device.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [Animating and Denoising a Raytraced Scene](animating_and_denoising_a_raytraced_scene.md)
  Support dynamic scenes and denoising by extending your ray tracer with Metal Performance Shaders.
- [class MPSRayIntersector](mpsrayintersector.md)
  A kernel that performs intersection tests between rays and geometry.
- [class MPSInstanceAccelerationStructure](mpsinstanceaccelerationstructure.md)
  An acceleration structure built over instances of other acceleration structures.
- [class MPSTriangleAccelerationStructure](mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.
- [class MPSAccelerationStructure](mpsaccelerationstructure.md)
  The base class for data structures that are built over geometry and used to accelerate ray tracing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructuregroup)*