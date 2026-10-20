# USDPrim.Attribute.ValueType

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A type that describes the kind of value an attribute can store, such as `float3` or `token[]`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ValueType
```

## Topics

### Instance Properties
- [var array: USDPrim.Attribute.ValueType](./valuetype/array.md)
  The array type corresponding to this type.
- [var role: USDToken](./valuetype/role.md)
  The name of this type’s role, if it has one.
- [var scalar: USDPrim.Attribute.ValueType](./valuetype/scalar.md)
  The scalar (non-array) type corresponding to this type.
### Type Properties
- [static var asset: USDPrim.Attribute.ValueType](./valuetype/asset.md)
- [static var bool: USDPrim.Attribute.ValueType](./valuetype/bool.md)
- [static var color3d: USDPrim.Attribute.ValueType](./valuetype/color3d.md)
- [static var color3f: USDPrim.Attribute.ValueType](./valuetype/color3f.md)
- [static var color3h: USDPrim.Attribute.ValueType](./valuetype/color3h.md)
- [static var color4d: USDPrim.Attribute.ValueType](./valuetype/color4d.md)
- [static var color4f: USDPrim.Attribute.ValueType](./valuetype/color4f.md)
- [static var color4h: USDPrim.Attribute.ValueType](./valuetype/color4h.md)
- [static var double: USDPrim.Attribute.ValueType](./valuetype/double.md)
- [static var double2: USDPrim.Attribute.ValueType](./valuetype/double2.md)
- [static var double3: USDPrim.Attribute.ValueType](./valuetype/double3.md)
- [static var double4: USDPrim.Attribute.ValueType](./valuetype/double4.md)
- [static var float: USDPrim.Attribute.ValueType](./valuetype/float.md)
- [static var float2: USDPrim.Attribute.ValueType](./valuetype/float2.md)
- [static var float3: USDPrim.Attribute.ValueType](./valuetype/float3.md)
- [static var float4: USDPrim.Attribute.ValueType](./valuetype/float4.md)
- [static var frame4d: USDPrim.Attribute.ValueType](./valuetype/frame4d.md)
- [static var group: USDPrim.Attribute.ValueType](./valuetype/group.md)
- [static var half: USDPrim.Attribute.ValueType](./valuetype/half.md)
- [static var half2: USDPrim.Attribute.ValueType](./valuetype/half2.md)
- [static var half3: USDPrim.Attribute.ValueType](./valuetype/half3.md)
- [static var half4: USDPrim.Attribute.ValueType](./valuetype/half4.md)
- [static var int2: USDPrim.Attribute.ValueType](./valuetype/int2.md)
- [static var int3: USDPrim.Attribute.ValueType](./valuetype/int3.md)
- [static var int32: USDPrim.Attribute.ValueType](./valuetype/int32.md)
- [static var int4: USDPrim.Attribute.ValueType](./valuetype/int4.md)
- [static var int64: USDPrim.Attribute.ValueType](./valuetype/int64.md)
- [static var invalid: USDPrim.Attribute.ValueType](./valuetype/invalid.md)
  An invalid value type.
- [static var matrix2d: USDPrim.Attribute.ValueType](./valuetype/matrix2d.md)
- [static var matrix3d: USDPrim.Attribute.ValueType](./valuetype/matrix3d.md)
- [static var matrix4d: USDPrim.Attribute.ValueType](./valuetype/matrix4d.md)
- [static var normal3d: USDPrim.Attribute.ValueType](./valuetype/normal3d.md)
- [static var normal3f: USDPrim.Attribute.ValueType](./valuetype/normal3f.md)
- [static var normal3h: USDPrim.Attribute.ValueType](./valuetype/normal3h.md)
- [static var opaque: USDPrim.Attribute.ValueType](./valuetype/opaque.md)
- [static var pathExpression: USDPrim.Attribute.ValueType](./valuetype/pathexpression.md)
- [static var point3d: USDPrim.Attribute.ValueType](./valuetype/point3d.md)
- [static var point3f: USDPrim.Attribute.ValueType](./valuetype/point3f.md)
- [static var point3h: USDPrim.Attribute.ValueType](./valuetype/point3h.md)
- [static var quatd: USDPrim.Attribute.ValueType](./valuetype/quatd.md)
- [static var quatf: USDPrim.Attribute.ValueType](./valuetype/quatf.md)
- [static var quath: USDPrim.Attribute.ValueType](./valuetype/quath.md)
- [static var string: USDPrim.Attribute.ValueType](./valuetype/string.md)
- [static var textureCoordinate2d: USDPrim.Attribute.ValueType](./valuetype/texturecoordinate2d.md)
- [static var textureCoordinate2f: USDPrim.Attribute.ValueType](./valuetype/texturecoordinate2f.md)
- [static var textureCoordinate2h: USDPrim.Attribute.ValueType](./valuetype/texturecoordinate2h.md)
- [static var textureCoordinate3d: USDPrim.Attribute.ValueType](./valuetype/texturecoordinate3d.md)
- [static var textureCoordinate3f: USDPrim.Attribute.ValueType](./valuetype/texturecoordinate3f.md)
- [static var textureCoordinate3h: USDPrim.Attribute.ValueType](./valuetype/texturecoordinate3h.md)
- [static var timeCode: USDPrim.Attribute.ValueType](./valuetype/timecode.md)
- [static var token: USDPrim.Attribute.ValueType](./valuetype/token.md)
- [static var uchar: USDPrim.Attribute.ValueType](./valuetype/uchar.md)
- [static var uint32: USDPrim.Attribute.ValueType](./valuetype/uint32.md)
- [static var uint64: USDPrim.Attribute.ValueType](./valuetype/uint64.md)
- [static var vector3d: USDPrim.Attribute.ValueType](./valuetype/vector3d.md)
- [static var vector3f: USDPrim.Attribute.ValueType](./valuetype/vector3f.md)
- [static var vector3h: USDPrim.Attribute.ValueType](./valuetype/vector3h.md)
### Type Methods
- [static func type(named: USDToken) -> USDPrim.Attribute.ValueType](./valuetype/type%28named%29.md)
  The type corresponding to the given type name.
### Enumerations
- [USDPrim.Attribute.ValueType.TupleDimensions](./valuetype/tupledimensions.md)
  The shape of a value type’s components.
### Default Implementations
- [CustomStringConvertible Implementations](./valuetype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/valuetype)*