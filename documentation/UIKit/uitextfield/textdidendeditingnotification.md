# textDidEndEditingNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that alerts observers when the editing session ends for a text field.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
nonisolated
class let textDidEndEditingNotification: NSNotification.Name
```

```c
extern NSNotificationName const UITextFieldTextDidEndEditingNotification;
```

#### Discussion

The affected text field is stored in the `object` parameter of the notification. The `userInfo` dictionary is not used.

## See Also

### Managing the editing behavior
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
- [var clearsOnBeginEditing: Bool](./clearsonbeginediting.md)
  A Boolean value that determines whether the text field removes old text when editing begins.
- [var clearsOnInsertion: Bool](./clearsoninsertion.md)
  A Boolean value that determines whether inserting text replaces the previous contents.
- [var allowsEditingTextAttributes: Bool](./allowseditingtextattributes.md)
  A Boolean value that determines whether the user can edit the attributes of the text in the text field.
- [UITextField.DidEndEditingReason](./didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.
- [class let didEndEditingReasonUserInfoKey: String](./didendeditingreasonuserinfokey.md)
  A key that indicates the reason for ending editing in a text field.
- [class let textDidBeginEditingNotification: NSNotification.Name](./textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text field.
- [class let textDidChangeNotification: NSNotification.Name](./textdidchangenotification.md)
  A notification that alerts observers when the text in a text field changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/textdidendeditingnotification)*