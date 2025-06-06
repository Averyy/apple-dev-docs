# textContainerInset

**Framework**: UIKit  
**Kind**: property

The inset of the text container’s layout area within the text view’s content area.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textContainerInset: UIEdgeInsets { get set }
```

#### Discussion

This property provides text margins for text laid out in the text view. By default the value of this property is `(8, 0, 8, 0)`.

## See Also

- [var usesStandardTextScaling: Bool](uitextview/usesstandardtextscaling.md)
  A Boolean value that determines the rendering scale of the text.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textcontainerinset)*