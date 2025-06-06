# percentComplete

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var percentComplete: CGFloat { get }
```

#### Return Value

The percentage of completion when an interactive transition moves to its noninteractive completion phase.

#### Discussion

Use this value to determine how much of the interactive transition completed before the transition was canceled or moved to its final animations.

## See Also

- [var presentationStyle: UIModalPresentationStyle](uiviewcontrollertransitioncoordinatorcontext/presentationstyle.md)
  The presentation style to use for the transition.
- [var transitionDuration: TimeInterval](uiviewcontrollertransitioncoordinatorcontext/transitionduration.md)
  Returns the noninteractive duration of a transition.
- [var completionCurve: UIView.AnimationCurve](uiviewcontrollertransitioncoordinatorcontext/completioncurve.md)
  Returns the completion curve associated with the transition.
- [var completionVelocity: CGFloat](uiviewcontrollertransitioncoordinatorcontext/completionvelocity.md)
  Returns the starting velocity to use for any final animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/percentcomplete)*