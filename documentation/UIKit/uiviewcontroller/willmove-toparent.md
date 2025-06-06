# willMove(toParent:)

**Framework**: UIKit  
**Kind**: method

Called just before the view controller is added or removed from a container view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func willMove(toParent parent: UIViewController?)
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Discussion

Your view controller can override this method when it needs to know that it has been added to a container.

If you are implementing your own container view controller, it must call the [`willMove(toParent:)`](uiviewcontroller/willmove(toparent:).md) method of the child view controller before calling the [`removeFromParent()`](uiviewcontroller/removefromparent().md) method, passing in a parent value of `nil`.

When your custom container calls the [`addChild(_:)`](uiviewcontroller/addchild(_:).md) method, it automatically calls the [`willMove(toParent:)`](uiviewcontroller/willmove(toparent:).md) method of the view controller to be added as a child before adding it.

## Parameters

- `parent`: The parent view controller, or   if there is no parent.

## See Also

- [func didMove(toParent: UIViewController?)](uiviewcontroller/didmove(toparent:).md)
  Called after the view controller is added or removed from a container view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/willmove(toparent:))*