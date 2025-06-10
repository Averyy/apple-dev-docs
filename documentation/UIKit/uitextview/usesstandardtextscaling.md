# usesStandardTextScaling

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines the rendering scale of the text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var usesStandardTextScaling: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), UIKit automatically adjusts the rendering of the text in the text view to match the standard text scaling.

When using the standard text scaling, font sizes in the text view appear visually similar to how they would render in macOS and non-Apple platforms, and copying the contents of the text view to the pasteboard preserves the original font point sizes. This effectively changes the display size of the text without changing the actual font point size. For example, text using a 13-point font in iOS looks like text using a 13-point font in macOS.

If your app is built with Mac Catalyst, or if your text view’s contents save to a document that a user can view in macOS or other platforms, set this property to [`true`](https://developer.apple.com/documentation/swift/true).

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [enum NSTextScalingType](nstextscalingtype.md)
  Constants that specify the text scaling.
- [static let textScaling: NSAttributedString.DocumentAttributeKey](../Foundation/NSAttributedString/DocumentAttributeKey/textScaling.md)
  The text-scaling mode to use when displaying the text.
- [static let sourceTextScaling: NSAttributedString.DocumentAttributeKey](../Foundation/NSAttributedString/DocumentAttributeKey/sourceTextScaling.md)
  The text-scaling mode you used when creating the text.
- [static let targetTextScaling: NSAttributedString.DocumentReadingOptionKey](../Foundation/NSAttributedString/DocumentReadingOptionKey/targetTextScaling.md)
  The text scaling mode to use after reading the text from disk.
- [static let sourceTextScaling: NSAttributedString.DocumentReadingOptionKey](../Foundation/NSAttributedString/DocumentReadingOptionKey/sourceTextScaling.md)
  The text-scaling mode to associate with the document’s content.
- [var textContainerInset: UIEdgeInsets](uitextview/textcontainerinset.md)
  The inset of the text container’s layout area within the text view’s content area.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/usesstandardtextscaling)*