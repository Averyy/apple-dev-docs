# definePrim(at:type:)

**Framework**: USDKit  
**Kind**: method

Defines a prim at a given path, if none already exists.

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
func definePrim(at path: USDLayer.Path, type: USDToken) -> USDPrim
```

#### Discussion

If a prim already exists at the given path, and that prim’s type is empty or equal to `type`, this function returns that prim. Otherwise, the prim authored by this function will be an [`USDPrim.Specifier.def`](usdprim/specifier-swift.enum/def.md) prim with the given type.

> **Note**: This function will also author any missing parent prims along the given `path`. Prims authored this way will have an empty type.

## Parameters

- `path`: An absolute path in this stage.
- `type`: The type name of the prim to define.

## See Also

- [func overridePrim(at: USDLayer.Path) -> USDPrim](usdstage/overrideprim(at:).md)
  Authors an override prim at a given path, if no prim exists at that path.
- [func removePrim(at: USDLayer.Path) -> Bool](usdstage/removeprim(at:).md)
  Removes all authored data at the given path in the current edit target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/defineprim(at:type:))*