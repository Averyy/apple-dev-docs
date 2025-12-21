# canPerformUnwindSegueAction(_:from:sender:)

**Framework**: UIKit  
**Kind**: method

Called on a view controller to determine whether it responds to an unwind action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func canPerformUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the view controller handles the unwind action, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When an unwind segue is triggered, UIKit uses this method and the [`allowedChildrenForUnwinding(from:)`](uiviewcontroller/allowedchildrenforunwinding(from:).md) method to locate a suitable view controller to handle the unwind segue.

The default implementation of this method returns [`true`](https://developer.apple.com/documentation/Swift/true) when the current view controller implements the `action` method and is not the same view controller as the one in the `fromViewController` parameter. You can override this method as needed to change the default behavior. For example, you might return [`false`](https://developer.apple.com/documentation/Swift/false) if the current view controller does not make a suitable return target when unwinding from the specified view controller.

## Parameters

- `action`: The unwind action to invoke on your view controller.
- `fromViewController`: The view controller that initiated the unwind action.
- `sender`: The object that triggered the action.

## See Also

- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](uiviewcontroller/shouldperformsegue(withidentifier:sender:).md)
  Determines whether the segue with the specified identifier should be performed.
- [func prepare(for: UIStoryboardSegue, sender: Any?)](uiviewcontroller/prepare(for:sender:).md)
  Notifies the view controller that a segue is about to be performed.
- [func performSegue(withIdentifier: String, sender: Any?)](uiviewcontroller/performsegue(withidentifier:sender:).md)
  Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [func allowedChildrenForUnwinding(from: UIStoryboardUnwindSegueSource) -> [UIViewController]](uiviewcontroller/allowedchildrenforunwinding(from:).md)
  Returns an array of child view controllers to search for an unwind segue destination.
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](uiviewcontroller/childcontaining(_:).md)
  Returns the child view controller that contains the source of the unwind segue.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](uiviewcontroller/unwind(for:towards:).md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/canperformunwindsegueaction(_:from:sender:))*