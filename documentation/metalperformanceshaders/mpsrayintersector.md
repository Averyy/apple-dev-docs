# MPSRayIntersector

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that performs intersection tests between rays and geometry.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class MPSRayIntersector : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsrayintersector/2998438-init.md)
- [init(device: any MTLDevice)](mpsrayintersector/2998439-init.md)
### Instance Properties
- [var boundingBoxIntersectionTestType: MPSBoundingBoxIntersectionTestType](mpsrayintersector/3013799-boundingboxintersectiontesttype.md)
- [var cullMode: MTLCullMode](mpsrayintersector/2998433-cullmode.md)
- [var frontFacingWinding: MTLWinding](mpsrayintersector/2998437-frontfacingwinding.md)
- [var intersectionDataType: MPSIntersectionDataType](mpsrayintersector/2998440-intersectiondatatype.md)
- [var intersectionStride: Int](mpsrayintersector/2998441-intersectionstride.md)
- [var rayDataType: MPSRayDataType](mpsrayintersector/2998443-raydatatype.md)
- [var rayIndexDataType: MPSDataType](mpsrayintersector/3131884-rayindexdatatype.md)
- [var rayMask: UInt32](mpsrayintersector/3152591-raymask.md)
- [var rayMaskOperator: MPSRayMaskOperator](mpsrayintersector/3242876-raymaskoperator.md)
- [var rayMaskOptions: MPSRayMaskOptions](mpsrayintersector/2998444-raymaskoptions.md)
- [var rayStride: Int](mpsrayintersector/2998445-raystride.md)
- [var triangleIntersectionTestType: MPSTriangleIntersectionTestType](mpsrayintersector/3013800-triangleintersectiontesttype.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrayintersector/2998432-copy.md)
- [func encode(with: NSCoder)](mpsrayintersector/2998436-encode.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCount: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/2998434-encodeintersection.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCountBuffer: any MTLBuffer, rayCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/2998435-encodeintersection.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCount: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/3131882-encodeintersection.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCountBuffer: any MTLBuffer, rayIndexCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/3131883-encodeintersection.md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayTexture: any MTLTexture, intersectionTexture: any MTLTexture, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/3143553-encodeintersection.md)
- [func recommendedMinimumRayBatchSize(rayCount: Int) -> Int](mpsrayintersector/2998446-recommendedminimumraybatchsize.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Animating and Denoising a Raytraced Scene](animating_and_denoising_a_raytraced_scene.md)
  Support dynamic scenes and denoising by extending your ray tracer with Metal Performance Shaders.
- [class MPSAccelerationStructureGroup](mpsaccelerationstructuregroup.md)
  A group of acceleration structures.
- [class MPSInstanceAccelerationStructure](mpsinstanceaccelerationstructure.md)
  An acceleration structure built over instances of other acceleration structures.
- [class MPSTriangleAccelerationStructure](mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.
- [class MPSAccelerationStructure](mpsaccelerationstructure.md)
  The base class for data structures that are built over geometry and used to accelerate ray tracing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrayintersector)*