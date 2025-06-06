# UIScribbleInteraction

**Framework**: UIKit  
**Kind**: class

An interaction for customizing the behavior of Scribble on text input views, or for suppressing it entirely in specific cases.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class UIScribbleInteraction
```

#### Overview

By default, Scribble lets users enter text by writing directly into any editable view that implements [`UITextInput`](uitextinput.md).

In apps with customized text fields, you can use the [`UIScribbleInteractionDelegate`](uiscribbleinteractiondelegate.md) callbacks to optimize the UI for a better writing experience. For example, you can hide custom placeholders when the user starts writing, or delay focusing on the field if it moves while gaining focus.

With text views that support drawing with Apple Pencil, you’ll need to suppress Scribble on nearby text fields to keep them from taking over the Pencil events for writing.

## Topics

### Creating a Scribble interaction
- [init(delegate: any UIScribbleInteractionDelegate)](uiscribbleinteraction/init(delegate:).md)
  Creates a Scribble interaction that allows customizing the behavior of Scribble on text input views with the delegate you provide.
### Managing Scribble interactions
- [var delegate: (any UIScribbleInteractionDelegate)?](uiscribbleinteraction/delegate.md)
  The object that acts as the delegate for this interaction and responds to Scribble events for text input views.
### Detecting writing
- [var isHandlingWriting: Bool](uiscribbleinteraction/ishandlingwriting.md)
  A Boolean value that indicates whether the user is actively writing in a text view.
### Expecting input from Apple Pencil
- [class var isPencilInputExpected: Bool](uiscribbleinteraction/ispencilinputexpected.md)
  A Boolean value that indicates the user is likely to use Apple Pencil and handwriting instead of the keyboard to enter text.

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
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UIScribbleInteractionDelegate](uiscribbleinteractiondelegate.md)
  Methods for customizing or suppressing Scribble behavior within text input views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteraction)*