# textPasteConfigurationSupporting(_:combineItemAttributedStrings:for:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to combine multiple strings into a single attributed string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, combineItemAttributedStrings itemStrings: [NSAttributedString], for textRange: UITextRange) -> NSAttributedString
```

#### Return Value

An attributed string based on the combination of multiple strings.

#### Discussion

You implement this method when you need to change how the item strings are combined to form the single attributed string. If this method isn’t implemented, the item strings are concatenated without any delimiters.

## Parameters

- `textPasteConfigurationSupporting`: The object that received the paste or drop request.
- `itemStrings`: An array of attributed strings that will be combined to form a single attributed string.
- `textRange`: The position in the text view where the paste or drop operation will place the text.

## See Also

- [func textPasteConfigurationSupporting(any UITextPasteConfigurationSupporting, performPasteOf: NSAttributedString, to: UITextRange) -> UITextRange](uitextpastedelegate/textpasteconfigurationsupporting(_:performpasteof:to:).md)
  Asks the delegate to explicitly handle the final incorporation of a pasted or dropped string of text into the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:combineitemattributedstrings:for:))*