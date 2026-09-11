# transform(at:)

**Framework**: USDKit  
**Kind**: method

Computes the prim’s composed local transform at the specified time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func transform(at time: USDStage.TimeCode = .default) -> USDValue.Matrix4d?
```

#### Return Value

The composed local transformation matrix, or `nil` if the prim is not transformable.

## Parameters

- `time`: The time at which to evaluate the transform. Defaults to `.default`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/transform(at:))*