# UITextPasteItem

**Framework**: UIKit  
**Kind**: protocol

The interface for obtaining information about, and interacting with, a text item for pasting or dropping.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextPasteItem : NSObjectProtocol
```

## Topics

### Accessing the text paste item’s data
- [var itemProvider: NSItemProvider](uitextpasteitem/itemprovider.md)
  The item provider for the item being pasted or dropped.
- [var localObject: Any?](uitextpasteitem/localobject.md)
  The custom local object that the copy or drag source optionally attached to the drag item.
### Getting the default attributes for a string
- [var defaultAttributes: [NSAttributedString.Key : Any]](uitextpasteitem/defaultattributes.md)
  The dictionary of default attributes that the system applies, during pasting or dropping, to plaintext strings from an item provider.
### Setting a text paste item’s result value
- [func setResult(string: String)](uitextpasteitem/setresult(string:).md)
  Sets a text paste item’s textual value to a specified plaintext string from the item provider.
- [func setResult(attributedString: NSAttributedString)](uitextpasteitem/setresult(attributedstring:).md)
  Sets a text paste item’s textual value to a specified attributed string from the item provider.
- [func setResult(attachment: NSTextAttachment)](uitextpasteitem/setresult(attachment:).md)
  Sets a text paste item’s attachment value to a specified value.
- [func setDefaultResult()](uitextpasteitem/setdefaultresult.md)
  Sets the text paste item’s value to the default value based on the item provider’s data.
- [func setNoResult()](uitextpasteitem/setnoresult.md)
  Sets the text paste item’s textual value to not include data from the item provider.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)

## See Also

- [protocol UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.
- [protocol UITextPasteDelegate](uitextpastedelegate.md)
  The interface for handling pasting and dropping of text, using item providers.
- [protocol UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
  The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpasteitem)*