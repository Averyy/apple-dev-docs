# allowsCopyingTokens

**Framework**: UIKit  
**Kind**: property

A Boolean that indicates whether the user can copy or drag tokens from the search field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsCopyingTokens: Bool { get set }
```

#### Discussion

The default value for this property is [`true`](https://developer.apple.com/documentation/swift/true).

To support copying tokens, [`allowsCopyingTokens`](uisearchtextfield/allowscopyingtokens.md) must be [`true`](https://developer.apple.com/documentation/swift/true) and the search field’s [`delegate`](uitextfield/delegate.md) must also implement [`searchTextField(_:itemProviderForCopying:)`](uisearchtextfielddelegate/searchtextfield(_:itemproviderforcopying:).md).

[`UISearchTextField`](uisearchtextfield.md) enables the Copy command when a user selects text, even if the selection also includes tokens and [`allowsCopyingTokens`](uisearchtextfield/allowscopyingtokens.md) is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var allowsDeletingTokens: Bool](uisearchtextfield/allowsdeletingtokens.md)
  A Boolean that indicates whether the user can remove tokens from the search field.
- [var delegate: (any UITextFieldDelegate)?](uitextfield/delegate.md)
  The text field’s delegate.
- [protocol UISearchTextFieldDelegate](uisearchtextfielddelegate.md)
  The interface for the delegate of a search field.
- [protocol UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/allowscopyingtokens)*