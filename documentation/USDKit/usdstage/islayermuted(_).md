# isLayerMuted(_:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the layer with the given identifier is muted.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func isLayerMuted(_ identifier: String) -> Bool
```

#### Return Value

`true` if the layer is muted; otherwise, `false`.

## Parameters

- `identifier`: The identifier of the layer to query.

## See Also

### Managing layers
- [var rootLayer: USDLayer](./rootlayer.md)
  The root layer of this stage.
- [func muteLayer(String)](./mutelayer%28_%29.md)
  Mutes the layer with the given identifier, excluding its opinions from composition.
- [func unmuteLayer(String)](./unmutelayer%28_%29.md)
  Unmutes the layer with the given identifier, restoring its opinions to composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/islayermuted(_:))*