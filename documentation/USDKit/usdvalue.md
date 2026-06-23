# USDValue

**Framework**: USDKit  
**Kind**: struct

A type-erased container for a value stored in a Universal Scene Description file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDValue
```

#### Overview

`USDValue` wraps the various concrete value types USD recognises (numerics, strings, vectors, tokens, paths, asset paths, time codes, and so on) so they can be passed through generic APIs without exposing the underlying C++ representation.

## Topics

### Creating a value
- [init()](usdvalue/init.md)
  Creates an empty value.
- [init<T>(T)](usdvalue/init(_:).md)
  Creates a value wrapping `value`.
### Accessing the value
- [func get<T>() -> T?](usdvalue/get.md)
  Returns the wrapped value if it is of type `T`, otherwise `nil`.
- [func uncheckedGet<T>() -> T](usdvalue/uncheckedget.md)
  Returns the wrapped value as `T` without checking the dynamic type.
- [func isHolding<T>(T.Type) -> Bool](usdvalue/isholding(_:).md)
  Returns whether this value holds a value of type `T`.
### Inspecting the value
- [var typeName: String](usdvalue/typename.md)
  The name of the wrapped type.
- [var isEmpty: Bool](usdvalue/isempty.md)
  Whether this value is empty.
- [var isArrayValued: Bool](usdvalue/isarrayvalued.md)
  Whether the wrapped value is an array.
- [var arraySize: Int](usdvalue/arraysize.md)
  The number of elements in the wrapped array, or `0` for scalar values.
- [USDValue.Vec3d](usdvalue/vec3d.md)
  A 3-component double-precision vector.
### Structures
- [USDValue.Matrix2d](usdvalue/matrix2d.md)
  A 2x2 matrix of double-precision floating-point values.
- [USDValue.Matrix2f](usdvalue/matrix2f.md)
  A 2x2 matrix of single-precision floating-point values.
- [USDValue.Matrix3d](usdvalue/matrix3d.md)
  A 3x3 matrix of double-precision floating-point values.
- [USDValue.Matrix3f](usdvalue/matrix3f.md)
  A 3x3 matrix of single-precision floating-point values.
- [USDValue.Matrix4d](usdvalue/matrix4d.md)
  A 4x4 matrix of double-precision floating-point values.
- [USDValue.Matrix4f](usdvalue/matrix4f.md)
  A 4x4 matrix of single-precision floating-point values.
- [USDValue.Quatd](usdvalue/quatd.md)
- [USDValue.Quatf](usdvalue/quatf.md)
- [USDValue.Quath](usdvalue/quath.md)
  A half-precision quaternion.
- [USDValue.Vec2d](usdvalue/vec2d.md)
  A 2-component double-precision vector.
- [USDValue.Vec2f](usdvalue/vec2f.md)
  A 2-component single-precision vector.
- [USDValue.Vec2h](usdvalue/vec2h.md)
  A 2-component half-precision vector.
- [USDValue.Vec2i](usdvalue/vec2i.md)
  A 2-component 32-bit integer vector.
- [USDValue.Vec3f](usdvalue/vec3f.md)
  A 3-component single-precision vector.
- [USDValue.Vec3h](usdvalue/vec3h.md)
  A 3-component half-precision vector.
- [USDValue.Vec3i](usdvalue/vec3i.md)
  A 3-component 32-bit integer vector.
- [USDValue.Vec4d](usdvalue/vec4d.md)
  A 4-component double-precision vector.
- [USDValue.Vec4f](usdvalue/vec4f.md)
  A 4-component single-precision vector.
- [USDValue.Vec4h](usdvalue/vec4h.md)
  A 4-component half-precision vector.
- [USDValue.Vec4i](usdvalue/vec4i.md)
  A 4-component 32-bit integer vector.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [protocol USDValueProtocol](usdvalueprotocol.md)
  A type that can be wrapped in a [`USDValue`](usdvalue.md).
- [struct USDToken](usdtoken.md)
  An interned, efficiently compared string that names prims, properties, and other scene-description identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue)*