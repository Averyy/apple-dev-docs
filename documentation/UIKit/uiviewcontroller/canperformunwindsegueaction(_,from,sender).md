# canPerformUnwindSegueAction(_:from:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called on a view controller to determine whether it responds to an unwind action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func canPerformUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, sender: Any?) -> Bool
```

```objc
- (BOOL) canPerformUnwindSegueAction:(SEL) action fromViewController:(UIViewController *) fromViewController sender:(id) sender;
```

## Return Value

[`true`](../../Swift/true.md) if the view controller handles the unwind action, otherwise [`false`](../../Swift/false.md).

## Discussion

When an unwind segue is triggered, UIKit uses this method and the [`allowedChildrenForUnwinding(from:)`](./allowedchildrenforunwinding%28from%29.md) method to locate a suitable view controller to handle the unwind segue.

The default implementation of this method returns [`true`](../../Swift/true.md) when the current view controller implements the `action` method and is not the same view controller as the one in the `fromViewController` parameter. You can override this method as needed to change the default behavior. For example, you might return [`false`](../../Swift/false.md) if the current view controller does not make a suitable return target when unwinding from the specified view controller.

## Parameters

- `action`: The unwind action to invoke on your view controller.
- `fromViewController`: The view controller that initiated the unwind action.
- `sender`: The object that triggered the action.

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
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](./childcontaining%28_%29.md)
  Returns the child view controller that contains the source of the unwind segue.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](./unwind%28for,towards%29.md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/canperformunwindsegueaction(_:from:sender:))*