# allowsDeletingTokens

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user can remove tokens from the search field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsDeletingTokens: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsDeletingTokens;
```

#### Discussion

The default value for this property is [`true`](../../Swift/true.md).

You can always remove tokens programmatically. When this value is [`true`](../../Swift/true.md), the user can also delete tokens and your app needs to handle tokens being re-added to the field with Undo.

## See Also

### Supporting token interactions
- [var allowsCopyingTokens: Bool](./allowscopyingtokens.md)
  A Boolean that indicates whether the user can copy or drag tokens from the search field.
- [var delegate: (any UITextFieldDelegate)?](../uitextfield/delegate.md)
  The text field’s delegate.
- [protocol UISearchTextFieldDelegate](../uisearchtextfielddelegate.md)
  The interface for the delegate of a search field.
- [protocol UISearchTextFieldPasteItem](../uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/allowsdeletingtokens)*