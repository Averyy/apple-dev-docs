# UITextCursorDropPositionAnimator

**Framework**: UIKit  
**Kind**: class

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
class UITextCursorDropPositionAnimator
```

## Topics

### Initializers
- [init!(textCursorView: (any UIView & UITextCursorView)!, textInput: (any UIView & UITextInput)!)](uitextcursordroppositionanimator/init(textcursorview:textinput:).md)
### Instance Properties
- [var cursorView: (any UIView & UITextCursorView)!](uitextcursordroppositionanimator/cursorview.md)
- [var textInput: (any UIView & UITextInput)!](uitextcursordroppositionanimator/textinput.md)
### Instance Methods
- [func animate(alongsideChanges: (() -> Void)?, completion: (() -> Void)?)](uitextcursordroppositionanimator/animate(alongsidechanges:completion:).md)
- [func placeCursor(at: UITextPosition!, animated: Bool)](uitextcursordroppositionanimator/placecursor(at:animated:).md)
- [func setCursorVisible(Bool, animated: Bool)](uitextcursordroppositionanimator/setcursorvisible(_:animated:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [class UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHighlightView](uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextSelectionHandleView](uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextLoupeSession](uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursordroppositionanimator)*