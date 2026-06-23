# primPath

**Framework**: USDKit  
**Kind**: property

The complete path to this prim, or to the nearest prim that contains this object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var primPath: USDLayer.Path { get }
```

#### Discussion

If this object is a [`USDPrim`](usdprim.md), `primPath` is the same as [`path`](usdstage/object/path.md). If this object is a `UsdAttribute` or a `UsdRelationship`, `primPath` is the complete scene path of the object’s [`prim`](usdstage/object/prim.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/primpath)*