# textDidBeginEditingNotification

**Framework**: UIKit  
**Kind**: property

A notification that alerts observers when an editing session begins in a text view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
nonisolated
class let textDidBeginEditingNotification: NSNotification.Name
```

#### Discussion

The affected view is stored in the `object` parameter of the notification. The `userInfo` dictionary is not used.

## See Also

- [var isEditable: Bool](uitextview/iseditable.md)
  A Boolean value that indicates whether the text view is editable.
- [var allowsEditingTextAttributes: Bool](uitextview/allowseditingtextattributes.md)
  A Boolean value that indicates whether the text view allows the user to edit style information.
- [class let textDidChangeNotification: NSNotification.Name](uitextview/textdidchangenotification.md)
  A notification that alerts observers when the text in a text view changes.
- [class let textDidEndEditingNotification: NSNotification.Name](uitextview/textdidendeditingnotification.md)
  A notification that alerts observers when the editing session ends for a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textdidbegineditingnotification)*