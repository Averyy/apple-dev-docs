# withEditTarget(layer:_:)

**Framework**: USDKit  
**Kind**: method

Performs the closure with the stage’s edit target set to author into the currently selected variant.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func withEditTarget<R>(layer: USDLayer? = nil, _ body: (USDStage.EditTarget) throws -> R) rethrows -> R
```

#### Return Value

The value returned by `body`.

#### Discussion

The previous edit target is restored when the closure returns.

> **Note**: Errors from `body` are rethrown.

## Parameters

- `layer`: The layer to target, or `nil` for the current edit target’s layer.
- `body`: A closure that performs edits within the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantset/withedittarget(layer:_:))*