# property(at:)

**Framework**: USDKit  
**Kind**: method

Returns the property spec at the given path within this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func property(at path: USDLayer.Path) -> USDPrim.Property.Spec?
```

#### Return Value

The property spec, or `nil` if none exists at `path`.

## Parameters

- `path`: The path to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/spec/property(at:))*