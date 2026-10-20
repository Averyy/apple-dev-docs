# clearsOnBeginEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the text field removes old text when editing begins.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearsOnBeginEditing: Bool { get set }
```

```objc
@property (nonatomic) BOOL clearsOnBeginEditing;
```

#### Discussion

If this property is set to [`true`](../../Swift/true.md), the text field’s previous text is cleared when the user selects the text field to begin editing. If [`false`](../../Swift/false.md), the text field places an insertion point at the place where the user tapped the field.

> **Note**:  Even if this property is set to [`true`](../../Swift/true.md), the text field delegate can override this behavior by returning [`false`](../../Swift/false.md) from its [`textFieldShouldClear(_:)`](../uitextfielddelegate/textfieldshouldclear%28_%29.md) method.

## See Also

### Managing the editing behavior
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the text field is currently in edit mode.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/clearsonbeginediting)*