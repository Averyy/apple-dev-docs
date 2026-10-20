# UITextCursorDropPositionAnimator

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UITextCursorDropPositionAnimator : NSObject
```

#### Overview

Provides a mechanism for displaying and animating a temporary text cursor to indicate a drop location.

For custom text view implementations that implement drag and drop functionality, use this animator providing either your own UITextCursorView implementation or a concrete implementation to indicate at which point in your document the dropped item will be inserted. Using this animator provides you with all of the default system animations for how the text cursor would behave.

## Topics

### Initializers
- [init!(textCursorView: (any UIView & UITextCursorView)!, textInput: (any UIView & UITextInput)!)](./uitextcursordroppositionanimator/init%28textcursorview,textinput%29.md)
  Creates an animator for the given text cursor view implementation, and the document object that implements the UITextInput protocol.
### Instance Properties
- [var cursorView: (any UIView & UITextCursorView)!](./uitextcursordroppositionanimator/cursorview.md)
  The cursor view to be animated.
- [var textInput: (any UIView & UITextInput)!](./uitextcursordroppositionanimator/textinput.md)
  The object that implements the UITextInput protocol, used to query for geometry information regarding cursor placement.
### Instance Methods
- [func animate(alongsideChanges: (() -> Void)?, completion: (() -> Void)?)](./uitextcursordroppositionanimator/animate%28alongsidechanges,completion%29.md)
  Optionally, provide an animation block or completion block to run alongside cursor appearance or position update animations.
- [func placeCursor(at: UITextPosition!, animated: Bool)](./uitextcursordroppositionanimator/placecursor%28at,animated%29.md)
  Controls the placement of the cursor, using @c textInput and @c position to compute the final frame for the cursor view.
- [func setCursorVisible(Bool, animated: Bool)](./uitextcursordroppositionanimator/setcursorvisible%28_,animated%29.md)
  Controls the visibility of the cursor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Custom text selection
- [Adopting system selection UI in custom text views](./adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [class UITextSelectionDisplayInteraction](./uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHighlightView](./uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextSelectionHandleView](./uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](./uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](./uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextLoupeSession](./uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursordroppositionanimator)*