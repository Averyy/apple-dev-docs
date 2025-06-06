# textPasteConfigurationSupporting(_:performPasteOf:to:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to explicitly handle the final incorporation of a pasted or dropped string of text into the text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, performPasteOf attributedString: NSAttributedString, to textRange: UITextRange) -> UITextRange
```

#### Return Value

A text range representing the position of the text added to the text view.

#### Discussion

You implement this method when you want to handle pasting the final attributed string into the text view. If you don’t implement this method, the standard paste mechanism is used. When adding the attributed string to the text view, be sure to place the text at the provided text range. Placing the string elsewhere in the text view may confuse the user.

## See Also

- [func textPasteConfigurationSupporting(any UITextPasteConfigurationSupporting, combineItemAttributedStrings: [NSAttributedString], for: UITextRange) -> NSAttributedString](uitextpastedelegate/textpasteconfigurationsupporting(_:combineitemattributedstrings:for:).md)
  Asks the delegate to combine multiple strings into a single attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:performpasteof:to:))*