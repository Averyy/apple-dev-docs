# isEditable

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text view is editable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (nonatomic, getter=isEditable) BOOL editable;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Managing the editing behavior
- [var allowsEditingTextAttributes: Bool](./allowseditingtextattributes.md)
  A Boolean value that indicates whether the text view allows the user to edit style information.
- [class let textDidBeginEditingNotification: NSNotification.Name](./textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text view.
- [class let textDidChangeNotification: NSNotification.Name](./textdidchangenotification.md)
  A notification that alerts observers when the text in a text view changes.
- [class let textDidEndEditingNotification: NSNotification.Name](./textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/iseditable)*