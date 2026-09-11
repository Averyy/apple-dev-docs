# muteLayer(_:)

**Framework**: USDKit  
**Kind**: method

Mutes the layer with the given identifier, excluding its opinions from composition.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func muteLayer(_ identifier: String)
```

## Parameters

- `identifier`: The identifier of the layer to mute.

## See Also

- [var rootLayer: USDLayer](usdstage/rootlayer.md)
  The root layer of this stage.
- [func unmuteLayer(String)](usdstage/unmutelayer(_:).md)
  Unmutes the layer with the given identifier, restoring its opinions to composition.
- [func isLayerMuted(String) -> Bool](usdstage/islayermuted(_:).md)
  Returns a Boolean value that indicates whether the layer with the given identifier is muted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/mutelayer(_:))*