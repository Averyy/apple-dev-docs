# UISelectionFeedbackGenerator

**Framework**: UIKit  
**Kind**: class

A concrete feedback generator subclass that creates haptics to indicate a change in selection.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UISelectionFeedbackGenerator
```

#### Overview

Use selection feedback to communicate movement through a series of discrete values. For example, you might trigger selection feedback to indicate that a UI element’s values are changing.

The following code example shows how to play selection feedback in response to a long-press gesture.

```swift
var feedback = UISelectionFeedbackGenerator()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Create a selection feedback object and associate it with the view.
    feedback = UISelectionFeedbackGenerator(view: view)
    
    // Add a custom long-press gesture to the view.
    let longPressGesture = UILongPressGestureRecognizer(target: self, action: #selector(longPress(_:)))
    longPressGesture.numberOfTouchesRequired = 2
    view.addGestureRecognizer(longPressGesture)
}

@objc
private func longPress(_ sender: UILongPressGestureRecognizer) {
    if sender.state == .began {
        // Play selection feedback to indicate a selection change.
        feedback.selectionChanged(at: sender.location(in: view))
        
        // Update the UI in response to a selection change.
        // ...
    }
}
```

For more information, read [`Playing haptic feedback in your app`](https://developer.apple.com/documentation/ApplePencil/playing-haptic-feedback-in-your-app).

## Topics

### Reporting selection changes
- [func selectionChanged()](uiselectionfeedbackgenerator/selectionchanged.md)
  Triggers selection feedback.
- [func selectionChanged(at: CGPoint)](uiselectionfeedbackgenerator/selectionchanged(at:).md)
  Triggers selection feedback at the specified location.

## Relationships

### Inherits From
- [UIFeedbackGenerator](uifeedbackgenerator.md)
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

- [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md)
  Provide tactile feedback when people perform certain actions in your app.
- [class UIFeedbackGenerator](uifeedbackgenerator.md)
  The abstract superclass for all feedback generators.
- [class UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [class UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [class UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiselectionfeedbackgenerator)*