# MPSInstanceAccelerationStructure

**Framework**: Metal Performance Shaders  
**Kind**: cl

An acceleration structure built over instances of other acceleration structures.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSInstanceAccelerationStructure : MPSAccelerationStructure
```

## Topics

### Instance Properties
- [var accelerationStructures: [MPSPolygonAccelerationStructure]?](mpsinstanceaccelerationstructure/2980787-accelerationstructures.md)
- [var instanceBuffer: (any MTLBuffer)?](mpsinstanceaccelerationstructure/2980788-instancebuffer.md)
- [var instanceBufferOffset: Int](mpsinstanceaccelerationstructure/2980789-instancebufferoffset.md)
- [var instanceCount: Int](mpsinstanceaccelerationstructure/2980790-instancecount.md)
- [var maskBuffer: (any MTLBuffer)?](mpsinstanceaccelerationstructure/2980791-maskbuffer.md)
- [var maskBufferOffset: Int](mpsinstanceaccelerationstructure/2980792-maskbufferoffset.md)
- [var transformBuffer: (any MTLBuffer)?](mpsinstanceaccelerationstructure/2980793-transformbuffer.md)
- [var transformBufferOffset: Int](mpsinstanceaccelerationstructure/2980794-transformbufferoffset.md)
- [var transformType: MPSTransformType](mpsinstanceaccelerationstructure/2980795-transformtype.md)

## Relationships

### Inherits From
- [MPSAccelerationStructure](mpsaccelerationstructure.md)

## See Also

- [Animating and Denoising a Raytraced Scene](animating_and_denoising_a_raytraced_scene.md)
  Support dynamic scenes and denoising by extending your ray tracer with Metal Performance Shaders.
- [class MPSRayIntersector](mpsrayintersector.md)
  A kernel that performs intersection tests between rays and geometry.
- [class MPSAccelerationStructureGroup](mpsaccelerationstructuregroup.md)
  A group of acceleration structures.
- [class MPSTriangleAccelerationStructure](mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.
- [class MPSAccelerationStructure](mpsaccelerationstructure.md)
  The base class for data structures that are built over geometry and used to accelerate ray tracing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsinstanceaccelerationstructure)*