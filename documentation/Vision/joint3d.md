# Joint3D

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

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
- [init(position: simd_float4x4, localPosition: simd_float4x4, identifer: String, parentJoint: String)](./joint3d/init%28position,localposition,identifer,parentjoint%29.md)
  Creates a 3D joint.
### Inspecting a joint
- [let localPosition: simd_float4x4](./joint3d/localposition.md)
  The joint position relative to the parent joint.
- [let position: simd_float4x4](./joint3d/position.md)
  The joint position relative to the camera.
- [let parentJoint: String](./joint3d/parentjoint.md)
  The parent joint in the observation.
- [let identifier: String](./joint3d/identifier.md)
  The name of the joint.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Joints
- [struct Joint](./joint.md)
  A pose joint represented as a normalized point in an image, along with a label and a confidence value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/joint3d)*