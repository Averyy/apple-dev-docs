# notifyWhenInteractionEnds(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Registers a block to be executed when a transition changes from interactive to non-interactive.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func notifyWhenInteractionEnds(_ handler: @escaping (any UIViewControllerTransitionCoordinatorContext) -> Void)
```

#### Discussion

Your block is executed both when the transition completes normally and when the user cancels the transition. In the case where the user cancels the transition, UIKit executes your `context` block, calls the [`viewWillDisappear(_:)`](uiviewcontroller/viewwilldisappear(_:).md) method on the presented view controller, and finally calls the [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) method on the original view controller to signal that it’s once again visible.

Inside your block, you can get the value of the [`isCancelled`](uiviewcontrollertransitioncoordinatorcontext/iscancelled.md) method of the transition coordinator context and use that value to determine the appropriate course of action. For example, if the transition was canceled, you might use this block to remove any extra views that were added to the view hierarchy by a previous call to [`animate(alongsideTransition:completion:)`](uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:).md) or [`animateAlongsideTransition(in:animation:completion:)`](uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:).md).

You can call this method multiple times to register multiple blocks. All of the registered blocks are executed when the transition state changes.

## Parameters

- `handler`: The block to execute when the transition changes from interactive to noninteractive. The block has no return value and takes the following parameter:

## See Also

- [func animate(alongsideTransition: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:).md)
  Runs the specified animations at the same time as the view controller transition animations.
- [func animateAlongsideTransition(in: UIView?, animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:).md)
  Runs the specified animations in a view that’s outside of the designated container view.
- [func notifyWhenInteractionChanges((any UIViewControllerTransitionCoordinatorContext) -> Void)](uiviewcontrollertransitioncoordinator/notifywheninteractionchanges(_:).md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionends(_:))*