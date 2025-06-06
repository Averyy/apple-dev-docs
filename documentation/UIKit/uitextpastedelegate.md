# UITextPasteDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for handling pasting and dropping of text, using item providers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextPasteDelegate : NSObjectProtocol
```

## Topics

### Preparing to paste a text paste item
- [func textPasteConfigurationSupporting(any UITextPasteConfigurationSupporting, transform: any UITextPasteItem)](uitextpastedelegate/textpasteconfigurationsupporting(_:transform:).md)
  Tells the delegate to transform the pasted or dropped text item.
### Pasting the text paste item
- [func textPasteConfigurationSupporting(any UITextPasteConfigurationSupporting, combineItemAttributedStrings: [NSAttributedString], for: UITextRange) -> NSAttributedString](uitextpastedelegate/textpasteconfigurationsupporting(_:combineitemattributedstrings:for:).md)
  Asks the delegate to combine multiple strings into a single attributed string.
- [func textPasteConfigurationSupporting(any UITextPasteConfigurationSupporting, performPasteOf: NSAttributedString, to: UITextRange) -> UITextRange](uitextpastedelegate/textpasteconfigurationsupporting(_:performpasteof:to:).md)
  Asks the delegate to explicitly handle the final incorporation of a pasted or dropped string of text into the text view.
### Animating the paste operation
- [func textPasteConfigurationSupporting(any UITextPasteConfigurationSupporting, shouldAnimatePasteOf: NSAttributedString, to: UITextRange) -> Bool](uitextpastedelegate/textpasteconfigurationsupporting(_:shouldanimatepasteof:to:).md)
  Asks the delegate if the paste or drop operation should be animated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UITextPasteItem](uitextpasteitem.md)
  The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [protocol UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.
- [protocol UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
  The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpastedelegate)*