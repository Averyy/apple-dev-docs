# clearsOnInsertion

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether inserting text replaces the previous contents.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearsOnInsertion: Bool { get set }
```

```objc
@property (nonatomic) BOOL clearsOnInsertion;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md). When the value of this property is [`true`](../../Swift/true.md) and the text field is in editing mode, the selection UI is hidden and inserting new text clears the contents of the text field and sets the value of this property back to [`false`](../../Swift/false.md).

## See Also

### Managing the editing behavior
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
- [var clearsOnBeginEditing: Bool](./clearsonbeginediting.md)
  A Boolean value that determines whether the text field removes old text when editing begins.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/clearsoninsertion)*