# isEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the text field is currently in edit mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEditing: Bool { get }
```

#### Discussion

This property is set to [`true`](https://developer.apple.com/documentation/Swift/true) when the user begins editing text in this text field, and it is set to [`false`](https://developer.apple.com/documentation/Swift/false) again when editing ends. The text field notifies its delegate when editing begins and ends.

## See Also

- [var clearsOnBeginEditing: Bool](uitextfield/clearsonbeginediting.md)
  A Boolean value that determines whether the text field removes old text when editing begins.
- [var clearsOnInsertion: Bool](uitextfield/clearsoninsertion.md)
  A Boolean value that determines whether inserting text replaces the previous contents.
- [var allowsEditingTextAttributes: Bool](uitextfield/allowseditingtextattributes.md)
  A Boolean value that determines whether the user can edit the attributes of the text in the text field.
- [UITextField.DidEndEditingReason](uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.
- [class let didEndEditingReasonUserInfoKey: String](uitextfield/didendeditingreasonuserinfokey.md)
  A key that indicates the reason for ending editing in a text field.
- [class let textDidBeginEditingNotification: NSNotification.Name](uitextfield/textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text field.
- [class let textDidChangeNotification: NSNotification.Name](uitextfield/textdidchangenotification.md)
  A notification that alerts observers when the text in a text field changes.
- [class let textDidEndEditingNotification: NSNotification.Name](uitextfield/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/isediting)*