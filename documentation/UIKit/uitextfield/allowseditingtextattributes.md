# allowsEditingTextAttributes

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the user can edit the attributes of the text in the text field.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsEditingTextAttributes: Bool { get set }
```

#### Discussion

If this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the user may edit the style information of the text. In addition, pasting styled text into the text field retains any embedded style information. If [`false`](https://developer.apple.com/documentation/swift/false), the text field prohibits the editing of style information and strips style information from any pasted text. However, you can still set the style information programmatically using the methods of this class.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isEditing: Bool](uitextfield/isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
- [var clearsOnBeginEditing: Bool](uitextfield/clearsonbeginediting.md)
  A Boolean value that determines whether the text field removes old text when editing begins.
- [var clearsOnInsertion: Bool](uitextfield/clearsoninsertion.md)
  A Boolean value that determines whether inserting text replaces the previous contents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/allowseditingtextattributes)*