# UITextInteraction

**Framework**: UIKit  
**Kind**: class

An interaction that provides text selection gestures and UI to custom text views.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextInteraction
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Overview

Use [`UITextInteraction`](uitextinteraction.md) to provide your custom text views the same text selection gestures and UI available in native text views like [`UITextView`](uitextview.md) and [`UITextField`](uitextfield.md). When creating a text interaction, choose a mode that matches the state of the text, [`UITextInteractionMode.editable`](uitextinteractionmode/editable.md) or [`UITextInteractionMode.nonEditable`](uitextinteractionmode/noneditable.md). Then set the [`textInput`](uitextinteraction/textinput.md) property to an object that conforms to [`UITextInput`](uitextinput.md), and add the interaction to a view.

```swift
// Create a selection interaction for non-editable content.
let selectionInteraction = UITextInteraction(for: .nonEditable)

// Assign `textInput` to your view that implements the `UITextInput` protocol
// to get more control over the selection behavior and the text input system.
selectionInteraction.textInput = customTextView

// Add the interaction to the view.
customTextView.addInteraction(selectionInteraction)
```

If your custom text view supports editable and non-editable text, create two interactions — one for each mode — and add the interaction that matches the state of text to the view while removing the other interaction.

```swift
override func becomeFirstResponder() -> Bool {
    let isFirstResponder = self.isFirstResponder
    let result = super.becomeFirstResponder()
    
    if isFirstResponder == false && self.isFirstResponder == true {
        customTextView.removeInteraction(nonEditableTextInteraction)
        customTextView.addInteraction(editableTextInteraction)
    }
    
    return result
}

override func resignFirstResponder() -> Bool {
    let isFirstResponder = self.isFirstResponder
    let result = super.resignFirstResponder()
    
    if isFirstResponder == true && self.isFirstResponder == false {
        customTextView.removeInteraction(editableTextInteraction)
        customTextView.addInteraction(nonEditableTextInteraction)
    }
    
    return result
}
```

If your app provides other gestures in the same view hierarchy, you can use the [`require(toFail:)`](uigesturerecognizer/require(tofail:).md) method to set up failure requirements between your app’s gestures and the text interaction gestures listed in the [`gesturesForFailureRequirements`](uitextinteraction/gesturesforfailurerequirements.md) property.

## Topics

### Creating text interactions
- [convenience init(for: UITextInteractionMode)](uitextinteraction/init(for:).md)
  Creates a text interaction with the specified mode.
### Handling text input and interaction events
- [var textInput: (any UIResponder & UITextInput)?](uitextinteraction/textinput.md)
  The object that interacts with the text input system.
- [var delegate: (any UITextInteractionDelegate)?](uitextinteraction/delegate.md)
  The object that receives events from the text interaction.
- [protocol UITextInteractionDelegate](uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.
### Getting interaction information
- [var gesturesForFailureRequirements: [UIGestureRecognizer]](uitextinteraction/gesturesforfailurerequirements.md)
  The list of gestures that the text interaction adds to the view hierarchy.
- [var textInteractionMode: UITextInteractionMode](uitextinteraction/textinteractionmode.md)
  The mode of the text interaction.
- [enum UITextInteractionMode](uitextinteractionmode.md)
  Modes that determine the selection behaviors that a text interaction provides.

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

- [protocol UITextInteractionDelegate](uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.
- [enum UITextInteractionMode](uitextinteractionmode.md)
  Modes that determine the selection behaviors that a text interaction provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteraction)*