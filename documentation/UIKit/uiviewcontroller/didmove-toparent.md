# didMove(toParent:)

**Framework**: UIKit  
**Kind**: method

Called after the view controller is added or removed from a container view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func didMove(toParent parent: UIViewController?)
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Discussion

Your view controller can override this method when it wants to react to being added to a container.

If you are implementing your own container view controller, it must call the [`didMove(toParent:)`](uiviewcontroller/didmove(toparent:).md) method of the child view controller after the transition to the new controller is complete or, if there is no transition, immediately after calling the [`addChild(_:)`](uiviewcontroller/addchild(_:).md) method.

The [`removeFromParent()`](uiviewcontroller/removefromparent().md) method automatically calls the [`didMove(toParent:)`](uiviewcontroller/didmove(toparent:).md) method of the child view controller after it removes the child.

## Parameters

- `parent`: The parent view controller, or   if there is no parent.

## See Also

- [func willMove(toParent: UIViewController?)](uiviewcontroller/willmove(toparent:).md)
  Called just before the view controller is added or removed from a container view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/didmove(toparent:))*