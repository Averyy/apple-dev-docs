# overridePrim(at:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Authors an override prim at a given path, if no prim exists at that path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
func overridePrim(at path: USDLayer.Path) -> USDPrim
```

#### Discussion

If a prim already exists at the given path, this function returns that prim. If no prim exists at that path, the prim authored by this function will be an [`USDPrim.Specifier.over`](../usdprim/specifier-swift.enum/over.md) prim with no authored type.

> **Note**: Attributes on override prims change the values of attributes on regular `def` prims underneath them in the layer stack.

## See Also

### Authoring prims
- [func definePrim(at: USDLayer.Path, type: USDToken) -> USDPrim](./defineprim%28at,type%29.md)
  Defines a prim at a given path, if none already exists.
- [func removePrim(at: USDLayer.Path) -> Bool](./removeprim%28at%29.md)
  Removes all authored data at the given path in the current edit target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/overrideprim(at:))*