# childContaining(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the child view controller that contains the source of the unwind segue.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func childContaining(_ source: UIStoryboardUnwindSegueSource) -> UIViewController?
```

```objc
- (UIViewController *) childViewControllerContainingSegueSource:(UIStoryboardUnwindSegueSource *) source;
```

## Return Value

The view controller that contains the segue source.

## Discussion

Container view controllers call this method to identify the child view controller that is the source of the unwind segue. Typically, you call this method from your [`allowedChildrenForUnwinding(from:)`](./allowedchildrenforunwinding%28from%29.md) method so that you can remove the corresponding view controller from the returned list of children.

## Parameters

- `source`: The unwind segue source object containing information about the unwind segue.

## See Also

### Performing segues
- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](./shouldperformsegue%28withidentifier,sender%29.md)
  Determines whether the segue with the specified identifier should be performed.
- [func prepare(for: UIStoryboardSegue, sender: Any?)](./prepare%28for,sender%29.md)
  Notifies the view controller that a segue is about to be performed.
- [func performSegue(withIdentifier: String, sender: Any?)](./performsegue%28withidentifier,sender%29.md)
  Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [func allowedChildrenForUnwinding(from: UIStoryboardUnwindSegueSource) -> [UIViewController]](./allowedchildrenforunwinding%28from%29.md)
  Returns an array of child view controllers to search for an unwind segue destination.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](./canperformunwindsegueaction%28_,from,sender%29.md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](./unwind%28for,towards%29.md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childcontaining(_:))*