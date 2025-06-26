# MPSAccelerationStructure

**Framework**: Metal Performance Shaders  
**Kind**: class

The base class for data structures that are built over geometry and used to accelerate ray tracing.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSAccelerationStructure
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsaccelerationstructure/init(coder:device:).md)
- [init?(coder: NSCoder, group: MPSAccelerationStructureGroup)](mpsaccelerationstructure/init(coder:group:).md)
- [init(device: any MTLDevice)](mpsaccelerationstructure/init(device:).md)
- [init(group: MPSAccelerationStructureGroup)](mpsaccelerationstructure/init(group:).md)
### Instance Properties
- [var boundingBox: MPSAxisAlignedBoundingBox](mpsaccelerationstructure/boundingbox.md)
- [var group: MPSAccelerationStructureGroup](mpsaccelerationstructure/group.md)
- [var status: MPSAccelerationStructureStatus](mpsaccelerationstructure/status.md)
- [var usage: MPSAccelerationStructureUsage](mpsaccelerationstructure/usage.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsaccelerationstructure/copy(with:device:).md)
- [func copy(with: NSZone?, group: MPSAccelerationStructureGroup) -> Self](mpsaccelerationstructure/copy(with:group:).md)
- [func encode(with: NSCoder)](mpsaccelerationstructure/encode(with:).md)
- [func encodeRefit(commandBuffer: any MTLCommandBuffer)](mpsaccelerationstructure/encoderefit(commandbuffer:).md)
- [func rebuild()](mpsaccelerationstructure/rebuild.md)
- [func rebuild(completionHandler: (MPSAccelerationStructure?) -> Void)](mpsaccelerationstructure/rebuild(completionhandler:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSInstanceAccelerationStructure](mpsinstanceaccelerationstructure.md)
- [MPSPolygonAccelerationStructure](mpspolygonaccelerationstructure.md)
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