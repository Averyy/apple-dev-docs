# isEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text field is currently in edit mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isEditing: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isEditing) BOOL editing;
```

#### Discussion

This property is set to [`true`](../../Swift/true.md) when the user begins editing text in this text field, and it is set to [`false`](../../Swift/false.md) again when editing ends. The text field notifies its delegate when editing begins and ends.

## See Also

### Managing the editing behavior
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
- [class let textDidEndEditingNotification: NSNotification.Name](./textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/isediting)*