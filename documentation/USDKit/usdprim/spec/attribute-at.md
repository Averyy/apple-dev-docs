# attribute(at:)

**Framework**: USDKit  
**Kind**: method

Returns the attribute spec at the given path within this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func attribute(at path: USDLayer.Path) -> USDPrim.Attribute.Spec?
```

#### Return Value

The attribute spec, or `nil` if none exists at `path`.

## Parameters

- `path`: The path to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/spec/attribute(at:))*