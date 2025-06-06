# selectionChanged()

**Framework**: UIKit  
**Kind**: method

Triggers selection feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func selectionChanged()
```

#### Discussion

This method tells the generator that the user has changed a selection. In response, the generator may play the appropriate haptics. Don’t use this feedback when the user makes or confirms a selection; use it only when the selection changes.

For information on setting up a feedback generator, see the [`UIFeedbackGenerator`](uifeedbackgenerator.md) class.

## See Also

- [func prepare()](uifeedbackgenerator/prepare.md)
  Prepares the generator to trigger feedback.
- [func selectionChanged(at: CGPoint)](uiselectionfeedbackgenerator/selectionchanged(at:).md)
  Triggers selection feedback at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiselectionfeedbackgenerator/selectionchanged())*