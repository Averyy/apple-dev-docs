# UISearchTextFieldPasteItem

**Framework**: UIKit  
**Kind**: protocol

A protocol that supports pasting tokens.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UISearchTextFieldPasteItem : UITextPasteItem
```

#### Overview

When implementing [`textPasteConfigurationSupporting(_:transform:)`](uitextpastedelegate/textpasteconfigurationsupporting(_:transform:).md), your [`UITextPasteDelegate`](uitextpastedelegate.md) can decide whether to paste the item as text or as a token. If the [`UITextPasteItem`](uitextpasteitem.md) it receives is a [`UISearchTextFieldPasteItem`](uisearchtextfieldpasteitem.md), you can call [`setSearchTokenResult(_:)`](uisearchtextfieldpasteitem/setsearchtokenresult(_:).md) to prepare a token for pasting instead of text.

## Topics

### Providing a token
- [func setSearchTokenResult(UISearchToken)](uisearchtextfieldpasteitem/setsearchtokenresult(_:).md)
  Sets a paste item’s search token from an item provider.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UITextPasteItem](uitextpasteitem.md)

## See Also

- [protocol UITextPasteItem](uitextpasteitem.md)
  The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [protocol UITextPasteDelegate](uitextpastedelegate.md)
  The interface for handling pasting and dropping of text, using item providers.
- [protocol UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
  The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfieldpasteitem)*