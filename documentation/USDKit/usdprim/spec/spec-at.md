# spec(at:)

**Framework**: USDKit  
**Kind**: method

Returns the spec at the given path within this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func spec(at path: USDLayer.Path) -> USDLayer.Spec?
```

#### Return Value

The spec, or `nil` if no spec is authored at `path`.

## Parameters

- `path`: The path to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/spec/spec(at:))*