# UITextPasteConfigurationSupporting

**Framework**: UIKit  
**Kind**: protocol

The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextPasteConfigurationSupporting : UIPasteConfigurationSupporting
```

## Topics

### Setting the text paste delegate
- [var pasteDelegate: (any UITextPasteDelegate)?](uitextpasteconfigurationsupporting/pastedelegate.md)
  The text paste delegate that handles pasting and dropping of text, using item providers.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
### Inherited By
- [UITextDroppable](uitextdroppable.md)
### Conforming Types
- [UISearchTextField](uisearchtextfield.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)

## See Also

- [protocol UITextPasteItem](uitextpasteitem.md)
  The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [protocol UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.
- [protocol UITextPasteDelegate](uitextpastedelegate.md)
  The interface for handling pasting and dropping of text, using item providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpasteconfigurationsupporting)*