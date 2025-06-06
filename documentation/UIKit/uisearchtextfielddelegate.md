# UISearchTextFieldDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for the delegate of a search field.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UISearchTextFieldDelegate : UITextFieldDelegate
```

#### Overview

A search field asks its delegate for an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) when the user starts to copy or move a token. To support these interactions, set the search field’s [`delegate`](uitextfield/delegate.md) to an instance of [`UISearchTextFieldDelegate`](uisearchtextfielddelegate.md) that implements [`searchTextField(_:itemProviderForCopying:)`](uisearchtextfielddelegate/searchtextfield(_:itemproviderforcopying:).md) and set the search field’s [`allowsCopyingTokens`](uisearchtextfield/allowscopyingtokens.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

The search field’s [`pasteDelegate`](uitextpasteconfigurationsupporting/pastedelegate.md) handles pasting and dropping tokens as well as text.

## Topics

### Providing information to copy and drag
- [func searchTextField(UISearchTextField, itemProviderForCopying: UISearchToken) -> NSItemProvider](uisearchtextfielddelegate/searchtextfield(_:itemproviderforcopying:).md)
  Asks the delegate for an object that can provide a token when the copied token is pasted.
### Responding to search suggestion selections
- [func searchTextField(UISearchTextField, didSelect: any UISearchSuggestion)](uisearchtextfielddelegate/searchtextfield(_:didselect:).md)
  Tells the delegate when a person selects a search suggestion in the search text field.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UITextFieldDelegate](uitextfielddelegate.md)

## See Also

- [class UISearchTextField](uisearchtextfield.md)
  A view for displaying and editing text and search tokens.
- [class UISearchToken](uisearchtoken.md)
  Search criteria in a search text field, represented by text and an optional icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfielddelegate)*