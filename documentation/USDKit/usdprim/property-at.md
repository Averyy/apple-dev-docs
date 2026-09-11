# property(at:)

**Framework**: USDKit  
**Kind**: method

Returns the property at a given path, relative to this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func property(at path: USDLayer.Path) -> USDPrim.Property
```

#### Discussion

If `path` is relative, it is anchored to this prim’s path. If no property exists at the resolved path, returns an invalid property handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property(at:))*