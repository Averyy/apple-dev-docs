# unmuteLayer(_:)

**Framework**: USDKit  
**Kind**: method

Unmutes the layer with the given identifier, restoring its opinions to composition.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func unmuteLayer(_ identifier: String)
```

## Parameters

- `identifier`: The identifier of the layer to unmute.

## See Also

- [var rootLayer: USDLayer](usdstage/rootlayer.md)
  The root layer of this stage.
- [func muteLayer(String)](usdstage/mutelayer(_:).md)
  Mutes the layer with the given identifier, excluding its opinions from composition.
- [func isLayerMuted(String) -> Bool](usdstage/islayermuted(_:).md)
  Returns a Boolean value that indicates whether the layer with the given identifier is muted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/unmutelayer(_:))*