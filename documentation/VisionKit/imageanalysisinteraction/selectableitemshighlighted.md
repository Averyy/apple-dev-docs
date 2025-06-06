# selectableItemsHighlighted

**Framework**: Visionkit  
**Kind**: property

A Boolean value that indicates whether the interaction highlights actionable text or data the analyzer detects in text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var selectableItemsHighlighted: Bool { get set }
```

#### Discussion

The interaction object manages this property value for you. It sets this property to `false` if you set the [`analysis`](imageanalysisinteraction/analysis.md) property or the [`activeInteractionTypes`](imageanalysisinteraction/activeinteractiontypes.md) property to an empty set. Otherwise, it sets this property depending on whether a person toggles the Live Text button in the interface.

## See Also

- [var liveTextButtonVisible: Bool](imageanalysisinteraction/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](imageanalysisinteraction/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisinteraction/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisinteraction/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/selectableitemshighlighted)*