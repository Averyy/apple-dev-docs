# removePrim(at:)

**Framework**: USDKit  
**Kind**: method

Removes all authored data at the given path in the current edit target.

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
func removePrim(at path: USDLayer.Path) -> Bool
```

## See Also

- [func definePrim(at: USDLayer.Path, type: USDToken) -> USDPrim](usdstage/defineprim(at:type:).md)
  Defines a prim at a given path, if none already exists.
- [func overridePrim(at: USDLayer.Path) -> USDPrim](usdstage/overrideprim(at:).md)
  Authors an override prim at a given path, if no prim exists at that path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/removeprim(at:))*