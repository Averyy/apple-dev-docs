# allowedChildrenForUnwinding(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of child view controllers to search for an unwind segue destination.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func allowedChildrenForUnwinding(from source: UIStoryboardUnwindSegueSource) -> [UIViewController]
```

```objc
- (NSArray<UIViewController *> *) allowedChildViewControllersForUnwindingFromSource:(UIStoryboardUnwindSegueSource *) source;
```

## Mentions

- [Creating a custom container view controller](../creating-a-custom-container-view-controller.md)

#### Return Value

An array of view controllers representing the child view controllers to search. The order of the items in the array determines the search order.

#### Discussion

UIKit calls this method when searching for the destination of an unwind segue. The default implementation returns the contents of the [`children`](./children.md) property minus the view controller returned by the [`childContaining(_:)`](./childcontaining%28_%29.md) method. You can override this method as needed in your custom container view controllers to change the search order. For example, a navigation controller reverses the order so that the search starts with the view controller at the top of the navigation stack.

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
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](./childcontaining%28_%29.md)
  Returns the child view controller that contains the source of the unwind segue.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](./canperformunwindsegueaction%28_,from,sender%29.md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](./unwind%28for,towards%29.md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/allowedchildrenforunwinding(from:))*