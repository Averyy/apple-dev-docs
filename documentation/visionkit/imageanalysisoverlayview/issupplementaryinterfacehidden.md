# isSupplementaryInterfaceHidden

**Framework**: VisionKit  
**Kind**: property

A Boolean value that indicates whether the view hides supplementary interface objects.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var isSupplementaryInterfaceHidden: Bool { get set }
```

#### Discussion

Supplementary interface objects include the Live Text button and the interface for Quick Actions, depending on the item type. Setting this property invokes the [`setSupplementaryInterfaceHidden(_:animated:)`](imageanalysisoverlayview/setsupplementaryinterfacehidden(_:animated:).md) method, passing this property value and `true` for the animated parameter.

## See Also

- [var liveTextButtonVisible: Bool](imageanalysisoverlayview/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisoverlayview/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisoverlayview/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisoverlayview/selectableitemshighlighted.md)
  A Boolean value that indicates whether the overlay view highlights actionable text or data that the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/issupplementaryinterfacehidden)*