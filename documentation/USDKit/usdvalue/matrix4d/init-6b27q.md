# init(_:)

**Framework**: USDKit  
**Kind**: init

Creates a matrix from a Spatial projective transform (double-precision).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(_ projectiveTransform: ProjectiveTransform3D)
```

#### Discussion

`ProjectiveTransform3D` is column-major and treats vectors as column vectors; `Matrix4d` is row-major and treats vectors as row vectors. The in-memory layout is identical, so this initializer reads each `m[col, row]` element and lays it out row-major.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix4d/init(_:)-6b27q)*