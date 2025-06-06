# childContaining(_:)

**Framework**: UIKit  
**Kind**: method

Returns the child view controller that contains the source of the unwind segue.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func childContaining(_ source: UIStoryboardUnwindSegueSource) -> UIViewController?
```

#### Return Value

The view controller that contains the segue source.

#### Discussion

Container view controllers call this method to identify the child view controller that is the source of the unwind segue. Typically, you call this method from your [`allowedChildrenForUnwinding(from:)`](uiviewcontroller/allowedchildrenforunwinding(from:).md) method so that you can remove the corresponding view controller from the returned list of children.

## Parameters

- `source`: The unwind segue source object containing information about the unwind segue.

## See Also

- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](uiviewcontroller/shouldperformsegue(withidentifier:sender:).md)
  Determines whether the segue with the specified identifier should be performed.
- [func prepare(for: UIStoryboardSegue, sender: Any?)](uiviewcontroller/prepare(for:sender:).md)
  Notifies the view controller that a segue is about to be performed.
- [func performSegue(withIdentifier: String, sender: Any?)](uiviewcontroller/performsegue(withidentifier:sender:).md)
  Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [func allowedChildrenForUnwinding(from: UIStoryboardUnwindSegueSource) -> [UIViewController]](uiviewcontroller/allowedchildrenforunwinding(from:).md)
  Returns an array of child view controllers to search for an unwind segue destination.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](uiviewcontroller/canperformunwindsegueaction(_:from:sender:).md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](uiviewcontroller/unwind(for:towards:).md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childcontaining(_:))*