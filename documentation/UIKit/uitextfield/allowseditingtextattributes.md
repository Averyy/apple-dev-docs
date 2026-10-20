# allowsEditingTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user can edit the attributes of the text in the text field.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allowsEditingTextAttributes: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsEditingTextAttributes;
```

#### Discussion

If this property is set to [`true`](../../Swift/true.md), the user may edit the style information of the text. In addition, pasting styled text into the text field retains any embedded style information. If [`false`](../../Swift/false.md), the text field prohibits the editing of style information and strips style information from any pasted text. However, you can still set the style information programmatically using the methods of this class.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing the editing behavior
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
- [var clearsOnBeginEditing: Bool](./clearsonbeginediting.md)
  A Boolean value that determines whether the text field removes old text when editing begins.
- [var clearsOnInsertion: Bool](./clearsoninsertion.md)
  A Boolean value that determines whether inserting text replaces the previous contents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/allowseditingtextattributes)*