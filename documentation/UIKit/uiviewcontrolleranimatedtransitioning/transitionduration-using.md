# transitionDuration(using:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks your animator object for the duration (in seconds) of the transition animation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func transitionDuration(using transitionContext: (any UIViewControllerContextTransitioning)?) -> TimeInterval
```

#### Return Value

The duration, in seconds, of your custom transition animation.

#### Discussion

UIKit calls this method to obtain the timing information for your animations. The value you provide should be the same value that you use when configuring the animations in your [`animateTransition(using:)`](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md) method. UIKit uses the value to synchronize the actions of other objects that might be involved in the transition. For example, a navigation controller uses the value to synchronize changes to the navigation bar.

When determining the value to return, assume there will be no user interaction during the transition—even if you plan to support user interactions at runtime.

## Parameters

- `transitionContext`: The context object containing information to use during the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/transitionduration(using:))*