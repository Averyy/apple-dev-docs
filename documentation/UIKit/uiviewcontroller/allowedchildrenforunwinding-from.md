# allowedChildrenForUnwinding(from:)

**Framework**: UIKit  
**Kind**: method

Returns an array of child view controllers to search for an unwind segue destination.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func allowedChildrenForUnwinding(from source: UIStoryboardUnwindSegueSource) -> [UIViewController]
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Return Value

An array of view controllers representing the child view controllers to search. The order of the items in the array determines the search order.

#### Discussion

UIKit calls this method when searching for the destination of an unwind segue. The default implementation returns the contents of the [`children`](uiviewcontroller/children.md) property minus the view controller returned by the [`childContaining(_:)`](uiviewcontroller/childcontaining(_:).md) method. You can override this method as needed in your custom container view controllers to change the search order. For example, a navigation controller reverses the order so that the search starts with the view controller at the top of the navigation stack.

## Parameters

- `source`: The unwind segue source object containing information about the unwind segue.

## See Also

- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](uiviewcontroller/shouldperformsegue(withidentifier:sender:).md)
  Determines whether the segue with the specified identifier should be performed.
- [func prepare(for: UIStoryboardSegue, sender: Any?)](uiviewcontroller/prepare(for:sender:).md)
  Notifies the view controller that a segue is about to be performed.
- [func performSegue(withIdentifier: String, sender: Any?)](uiviewcontroller/performsegue(withidentifier:sender:).md)
  Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](uiviewcontroller/childcontaining(_:).md)
  Returns the child view controller that contains the source of the unwind segue.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](uiviewcontroller/canperformunwindsegueaction(_:from:sender:).md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](uiviewcontroller/unwind(for:towards:).md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/allowedchildrenforunwinding(from:))*