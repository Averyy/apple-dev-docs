# selectableItemsHighlighted

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the overlay view highlights actionable text or data that the analyzer detects in text.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var selectableItemsHighlighted: Bool { get set }
```

## Discussion

The overlay view manages this property value for you. It sets this property to `false` if you set the [`analysis`](./analysis.md) property or the [`activeInteractionTypes`](./activeinteractiontypes.md) property to an empty set. Otherwise, it sets this property depending on whether the user toggles the Live Text button in the interface.

## See Also

### Querying the interface state
- [var liveTextButtonVisible: Bool](./livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](./issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](./hasinteractiveitem%28at%29.md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](./hassupplementaryinterface%28at%29.md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/selectableitemshighlighted)*