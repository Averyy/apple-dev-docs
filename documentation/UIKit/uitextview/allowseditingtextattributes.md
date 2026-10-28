# allowsEditingTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text view allows the user to edit style information.

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

## Discussion

When set to [`true`](../../Swift/true.md), the text view allows the user to change the basic styling of the currently selected text. The available style options are listed in the edit menu and only apply to the selection.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing the editing behavior
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that indicates whether the text view is editable.
- [class let textDidBeginEditingNotification: NSNotification.Name](./textdidbegineditingnotification.md)
  A notification that alerts observers when an editing session begins in a text view.
- [class let textDidChangeNotification: NSNotification.Name](./textdidchangenotification.md)
  A notification that alerts observers when the text in a text view changes.
- [class let textDidEndEditingNotification: NSNotification.Name](./textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/allowseditingtextattributes)*