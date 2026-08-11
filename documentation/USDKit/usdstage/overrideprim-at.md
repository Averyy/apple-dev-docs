# overridePrim(at:)

**Framework**: USDKit  
**Kind**: method

Authors an override prim at a given path, if no prim exists at that path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func overridePrim(at path: USDLayer.Path) -> USDPrim
```

#### Discussion

If a prim already exists at the given path, this function returns that prim. If no prim exists at that path, the prim authored by this function will be an [`USDPrim.Specifier.over`](usdprim/specifier-swift.enum/over.md) prim with no authored type.

> **Note**: Attributes on override prims change the values of attributes on regular `def` prims underneath them in the layer stack.

## See Also

- [func definePrim(at: USDLayer.Path, type: USDToken) -> USDPrim](usdstage/defineprim(at:type:).md)
  Defines a prim at a given path, if none already exists.
- [func removePrim(at: USDLayer.Path) -> Bool](usdstage/removeprim(at:).md)
  Removes all authored data at the given path in the current edit target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/overrideprim(at:))*