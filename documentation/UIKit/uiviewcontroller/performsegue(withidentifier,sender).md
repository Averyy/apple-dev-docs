# performSegue(withIdentifier:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Initiates the segue with the specified identifier from the current view controller’s storyboard file.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func performSegue(withIdentifier identifier: String, sender: Any?)
```

```objc
- (void) performSegueWithIdentifier:(NSString *) identifier sender:(id) sender;
```

## Discussion

Normally, segues are initiated automatically and not using this method. However, you can use this method in cases where the segue could not be configured in your storyboard file. For example, you might call it from a custom action handler used in response to shake or accelerometer events.

The current view controller must have been loaded from a storyboard. If its [`storyboard`](./storyboard.md) property is `nil`, perhaps because you allocated and initialized the view controller yourself, this method throws an exception.

## Parameters

- `identifier`: The string that identifies the triggered segue. In Interface Builder, you specify the segue’s identifier string in the attributes inspector.

  This method throws an [Exception handling](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18) if there is no segue with the specified identifier.
- `sender`: The object that you want to use to initiate the segue. This object is made available for informational purposes during the actual segue.

## See Also

### Performing segues
- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](./shouldperformsegue%28withidentifier,sender%29.md)
  Determines whether the segue with the specified identifier should be performed.
- [func prepare(for: UIStoryboardSegue, sender: Any?)](./prepare%28for,sender%29.md)
  Notifies the view controller that a segue is about to be performed.
- [func allowedChildrenForUnwinding(from: UIStoryboardUnwindSegueSource) -> [UIViewController]](./allowedchildrenforunwinding%28from%29.md)
  Returns an array of child view controllers to search for an unwind segue destination.
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](./childcontaining%28_%29.md)
  Returns the child view controller that contains the source of the unwind segue.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](./canperformunwindsegueaction%28_,from,sender%29.md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](./unwind%28for,towards%29.md)
  Called when an unwind segue transitions to a new view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/performsegue(withidentifier:sender:))*