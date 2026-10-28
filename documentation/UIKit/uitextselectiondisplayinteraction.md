# UITextSelectionDisplayInteraction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that provides the system UI for displaying text selection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextSelectionDisplayInteraction
```

```objc
@interface UITextSelectionDisplayInteraction : NSObject
```

## Mentions

- [Adopting system selection UI in custom text views](./adopting-system-selection-ui-in-custom-text-views.md)

## Overview

> **Related sessions from WWDC23**:  Session 10058: [What’s new with text and text interactions](https://developer.apple.com/videos/play/wwdc2023/10058/)

## Topics

### Creating a text selection display interaction
- [init(textInput: any UITextInput, delegate: any UITextSelectionDisplayInteractionDelegate)](./uitextselectiondisplayinteraction/init%28textinput,delegate%29.md)
  Creates a new text selection display interaction object for the specified text view.
### Managing the drawing view
- [var delegate: (any UITextSelectionDisplayInteractionDelegate)?](./uitextselectiondisplayinteraction/delegate.md)
  A delegate that provides a container view to manage the system-supplied selection views.
- [protocol UITextSelectionDisplayInteractionDelegate](./uitextselectiondisplayinteractiondelegate.md)
  An object you use to customize the presentation of text selections in your interface.
### Activating the selection UI
- [var isActivated: Bool](./uitextselectiondisplayinteraction/isactivated.md)
  A Boolean value that indicates whether to display the system selection UI.
### Reporting changes to the selection
- [func setNeedsSelectionUpdate()](./uitextselectiondisplayinteraction/setneedsselectionupdate%28%29.md)
  Tells the system to update the selection UI to match the current selection state.
- [func layoutManagedSubviews()](./uitextselectiondisplayinteraction/layoutmanagedsubviews%28%29.md)
  Loads the selection from the text input view and lays out the selection-related views.
### Getting the text input view
- [var textInput: (any UITextInput)?](./uitextselectiondisplayinteraction/textinput.md)
  The text input object that manages the selection.
### Getting the system selection views
- [var highlightView: any UIView & UITextSelectionHighlightView](./uitextselectiondisplayinteraction/highlightview.md)
  The view that draws the selection highlight behind the rendered text.
- [var handleViews: [any UIView & UITextSelectionHandleView]](./uitextselectiondisplayinteraction/handleviews.md)
  The view that draws the selection handles for the selected text.
- [var cursorView: any UIView & UITextCursorView](./uitextselectiondisplayinteraction/cursorview.md)
  The view that draws the caret at the text insertion point.

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
- [UIInteraction](./uiinteraction.md)

## See Also

### Custom text selection
- [Adopting system selection UI in custom text views](./adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [protocol UITextSelectionHighlightView](./uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextSelectionHandleView](./uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](./uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](./uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextCursorDropPositionAnimator](./uitextcursordroppositionanimator.md)
- [class UITextLoupeSession](./uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction)*