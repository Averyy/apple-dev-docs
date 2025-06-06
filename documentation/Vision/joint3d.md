# Joint3D

**Framework**: Vision  
**Kind**: struct

An object that represents a body pose joint in 3D space.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Joint3D
```

## Topics

### Creating a joint
- [init(position: simd_float4x4, localPosition: simd_float4x4, identifer: String, parentJoint: String)](joint3d/init(position:localposition:identifer:parentjoint:).md)
  Creates a 3D joint.
### Inspecting a joint
- [let localPosition: simd_float4x4](joint3d/localposition.md)
  The joint position relative to the parent joint.
- [let position: simd_float4x4](joint3d/position.md)
  The joint position relative to the camera.
- [let parentJoint: String](joint3d/parentjoint.md)
  The parent joint in the observation.
- [let identifier: String](joint3d/identifier.md)
  The name of the joint.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class DetectHumanBodyPose3DRequest](detecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/joint3d)*