# delegate

**Framework**: Uikit  
**Kind**: property

The text field’s delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UITextFieldDelegate)? { get set }
```

#### Discussion

A text field delegate responds to editing-related messages from the text field. You can use the delegate to respond to the text entered by the user and to some special commands, such as when the user taps Return.

> **Note**:  If the text field is a [`UISearchTextField`](uisearchtextfield.md), set its delegate to an object that also conforms to the [`UISearchTextFieldDelegate`](uisearchtextfielddelegate.md) protocol.

## See Also

- [protocol UITextFieldDelegate](uitextfielddelegate.md)
  A set of optional methods to manage editing and validating text in a text field object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/delegate)*