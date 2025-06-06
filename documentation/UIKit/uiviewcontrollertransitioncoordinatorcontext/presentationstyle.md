# presentationStyle

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The presentation style to use for the transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var presentationStyle: UIModalPresentationStyle { get }
```

#### Return Value

The modal presentation style associated with the transition or [`UIModalPresentationStyle.none`](uimodalpresentationstyle/none.md) if the transition is not a modal presentation or dismissal. For a list of possible values, see “Modal Presentation Styles” in [`UIViewController`](uiviewcontroller.md).

#### Discussion

When presenting or dismissing a view controller modally, this method returns the presentation style used for that transition. For interface rotations and other events that don’t involve a specific transition between view controllers, this method returns [`UIModalPresentationStyle.none`](uimodalpresentationstyle/none.md).

## See Also

- [var transitionDuration: TimeInterval](uiviewcontrollertransitioncoordinatorcontext/transitionduration.md)
  Returns the noninteractive duration of a transition.
- [var completionCurve: UIView.AnimationCurve](uiviewcontrollertransitioncoordinatorcontext/completioncurve.md)
  Returns the completion curve associated with the transition.
- [var completionVelocity: CGFloat](uiviewcontrollertransitioncoordinatorcontext/completionvelocity.md)
  Returns the starting velocity to use for any final animations.
- [var percentComplete: CGFloat](uiviewcontrollertransitioncoordinatorcontext/percentcomplete.md)
  Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/presentationstyle)*