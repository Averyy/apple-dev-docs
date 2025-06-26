# MPSRayIntersector

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel that performs intersection tests between rays and geometry.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRayIntersector
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsrayintersector/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsrayintersector/init(device:).md)
### Instance Properties
- [var boundingBoxIntersectionTestType: MPSBoundingBoxIntersectionTestType](mpsrayintersector/boundingboxintersectiontesttype.md)
- [var cullMode: MTLCullMode](mpsrayintersector/cullmode.md)
- [var frontFacingWinding: MTLWinding](mpsrayintersector/frontfacingwinding.md)
- [var intersectionDataType: MPSIntersectionDataType](mpsrayintersector/intersectiondatatype.md)
- [var intersectionStride: Int](mpsrayintersector/intersectionstride.md)
- [var rayDataType: MPSRayDataType](mpsrayintersector/raydatatype.md)
- [var rayIndexDataType: MPSDataType](mpsrayintersector/rayindexdatatype.md)
- [var rayMask: UInt32](mpsrayintersector/raymask.md)
- [var rayMaskOperator: MPSRayMaskOperator](mpsrayintersector/raymaskoperator.md)
- [var rayMaskOptions: MPSRayMaskOptions](mpsrayintersector/raymaskoptions.md)
- [var rayStride: Int](mpsrayintersector/raystride.md)
- [var triangleIntersectionTestType: MPSTriangleIntersectionTestType](mpsrayintersector/triangleintersectiontesttype.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrayintersector/copy(with:device:).md)
- [func encode(with: NSCoder)](mpsrayintersector/encode(with:).md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCount: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raybuffer:raybufferoffset:intersectionbuffer:intersectionbufferoffset:raycount:accelerationstructure:).md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCountBuffer: any MTLBuffer, rayCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raybuffer:raybufferoffset:intersectionbuffer:intersectionbufferoffset:raycountbuffer:raycountbufferoffset:accelerationstructure:).md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCount: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raybuffer:raybufferoffset:rayindexbuffer:rayindexbufferoffset:intersectionbuffer:intersectionbufferoffset:rayindexcount:accelerationstructure:).md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCountBuffer: any MTLBuffer, rayIndexCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raybuffer:raybufferoffset:rayindexbuffer:rayindexbufferoffset:intersectionbuffer:intersectionbufferoffset:rayindexcountbuffer:rayindexcountbufferoffset:accelerationstructure:).md)
- [func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayTexture: any MTLTexture, intersectionTexture: any MTLTexture, accelerationStructure: MPSAccelerationStructure)](mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raytexture:intersectiontexture:accelerationstructure:).md)
- [func recommendedMinimumRayBatchSize(rayCount: Int) -> Int](mpsrayintersector/recommendedminimumraybatchsize(raycount:).md)

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

## See Also

- [Accelerating ray tracing and motion blur using Metal](../Metal/accelerating-ray-tracing-and-motion-blur-using-metal.md)
  Generate ray-traced images with motion blur using GPU-based parallel processing.
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