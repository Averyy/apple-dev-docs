# selectableItemsHighlighted

**Framework**: VisionKit  
**Kind**: property

A Boolean value that indicates whether the overlay view highlights actionable text or data that the analyzer detects in text.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var selectableItemsHighlighted: Bool { get set }
```

#### Discussion

The overlay view manages this property value for you. It sets this property to `false` if you set the [`analysis`](imageanalysisoverlayview/analysis.md) property or the [`activeInteractionTypes`](imageanalysisoverlayview/activeinteractiontypes.md) property to an empty set. Otherwise, it sets this property depending on whether the user toggles the Live Text button in the interface.

## See Also

- [var liveTextButtonVisible: Bool](imageanalysisoverlayview/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](imageanalysisoverlayview/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisoverlayview/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisoverlayview/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/selectableitemshighlighted)*