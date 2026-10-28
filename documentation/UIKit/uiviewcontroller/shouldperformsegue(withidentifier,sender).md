# shouldPerformSegue(withIdentifier:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the segue with the specified identifier should be performed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func shouldPerformSegue(withIdentifier identifier: String, sender: Any?) -> Bool
```

```objc
- (BOOL) shouldPerformSegueWithIdentifier:(NSString *) identifier sender:(id) sender;
```

## Mentions

- [Customizing the behavior of segue-based presentations](../customizing-the-behavior-of-segue-based-presentations.md)

## Return Value

[`true`](../../Swift/true.md) if the segue should be performed or [`false`](../../Swift/false.md) if it should be ignored.

## Discussion

Subclasses can override this method and use it to perform segues conditionally based on current conditions. If you do not implement this method, all segues are performed.

## Parameters

- `identifier`: The string that identifies the triggered segue. In Interface Builder, you specify the segue’s identifier string in the attributes inspector. This string is used only for locating the segue inside the storyboard.
- `sender`: The object that initiated the segue. This object is made available for informational purposes during the actual segue.

## See Also

### Performing segues
- [func prepare(for: UIStoryboardSegue, sender: Any?)](./prepare%28for,sender%29.md)
  Notifies the view controller that a segue is about to be performed.
- [func performSegue(withIdentifier: String, sender: Any?)](./performsegue%28withidentifier,sender%29.md)
  Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [func allowedChildrenForUnwinding(from: UIStoryboardUnwindSegueSource) -> [UIViewController]](./allowedchildrenforunwinding%28from%29.md)
  Returns an array of child view controllers to search for an unwind segue destination.
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](./childcontaining%28_%29.md)
  Returns the child view controller that contains the source of the unwind segue.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](./canperformunwindsegueaction%28_,from,sender%29.md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](./unwind%28for,towards%29.md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldperformsegue(withidentifier:sender:))*