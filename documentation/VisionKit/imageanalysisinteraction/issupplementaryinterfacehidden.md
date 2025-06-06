# isSupplementaryInterfaceHidden

**Framework**: Visionkit  
**Kind**: property

A Boolean value that indicates whether the view hides supplementary interface objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var isSupplementaryInterfaceHidden: Bool { get set }
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

Supplementary interface objects include the Live Text button and Quick Actions, depending on the item type. Setting this property invokes the [`setSupplementaryInterfaceHidden(_:animated:)`](imageanalysisinteraction/setsupplementaryinterfacehidden(_:animated:).md) method, passing this property value and `true` for the `animated` parameter.

## See Also

- [var liveTextButtonVisible: Bool](imageanalysisinteraction/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisinteraction/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisinteraction/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisinteraction/selectableitemshighlighted.md)
  A Boolean value that indicates whether the interaction highlights actionable text or data the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/issupplementaryinterfacehidden)*