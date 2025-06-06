# unwind(for:towards:)

**Framework**: UIKit  
**Kind**: method

Called when an unwind segue transitions to a new view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func unwind(for unwindSegue: UIStoryboardSegue, towards subsequentVC: UIViewController)
```

#### Discussion

During the execution of an unwind segue, UIKit calls this method on any view controllers in the unwind path to give them an opportunity to reconfigure themselves. Container view controllers must implement this method and use to display the view controller in the `subsequentVC` parameter. For example, a tab bar controller selects the tab containing the specified view controller. Noncontainer view controllers should not override this method.

## Parameters

- `unwindSegue`: The unwind segue being performed.
- `subsequentVC`: The view controller closest to the current controller that represents the transition direction. Container view controllers should configure themselves so that this view controller is displayed.

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
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](uiviewcontroller/canperformunwindsegueaction(_:from:sender:).md)
  Called on a view controller to determine whether it responds to an unwind action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/unwind(for:towards:))*