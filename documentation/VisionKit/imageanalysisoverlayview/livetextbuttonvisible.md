# liveTextButtonVisible

**Framework**: VisionKit  
**Kind**: property

A Boolean value that indicates whether the Live Text button appears.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var liveTextButtonVisible: Bool { get }
```

#### Discussion

When a person taps the Live Text button, it highlights recognized items in the image.

## See Also

- [var isSupplementaryInterfaceHidden: Bool](imageanalysisoverlayview/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisoverlayview/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisoverlayview/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisoverlayview/selectableitemshighlighted.md)
  A Boolean value that indicates whether the overlay view highlights actionable text or data that the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/livetextbuttonvisible)*