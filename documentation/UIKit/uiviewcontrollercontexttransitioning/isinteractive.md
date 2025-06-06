# isInteractive

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the transition is currently interactive.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isInteractive: Bool { get }
```

#### Discussion

A transition is interactive only if the view controller’s delegate provides a corresponding interactive animator object.

Interactive transitions are drive by user-generated events. One common scenario is to use a gesture recognizer to report on the current progress of the animation. The gesture recognizer calls methods of this context object that indicate the completion percentage of the transition or indicate that the transition was canceled or completed by the user.

## See Also

- [var isAnimated: Bool](uiviewcontrollercontexttransitioning/isanimated.md)
  A Boolean value indicating whether the transition should be animated.
- [var presentationStyle: UIModalPresentationStyle](uiviewcontrollercontexttransitioning/presentationstyle.md)
  Returns the presentation style for the view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/isinteractive)*