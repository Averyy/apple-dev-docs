# init(_:)

**Framework**: USDKit  
**Kind**: init

Creates a matrix from a Spatial projective transform (double-precision).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ projectiveTransform: ProjectiveTransform3D)
```

#### Discussion

`ProjectiveTransform3D` is column-major and treats vectors as column vectors; `Matrix4d` is row-major and treats vectors as row vectors. The in-memory layout is identical, so this initializer reads each `m[col, row]` element and lays it out row-major.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix4d/init(_:)-6b27q)*