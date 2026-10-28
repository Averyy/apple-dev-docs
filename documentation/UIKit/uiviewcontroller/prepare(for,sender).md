# prepare(for:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the view controller that a segue is about to be performed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
func prepare(for segue: UIStoryboardSegue, sender: Any?)
```

```objc
- (void) prepareForSegue:(UIStoryboardSegue *) segue sender:(id) sender;
```

## Mentions

- [Customizing the behavior of segue-based presentations](../customizing-the-behavior-of-segue-based-presentations.md)

## Discussion

The default implementation of this method does nothing. Subclasses override this method and use it to configure the new view controller prior to it being displayed. The segue object contains information about the transition, including references to both view controllers that are involved.

Because segues can be triggered from multiple sources, you can use the information in the `segue` and `sender` parameters to disambiguate between different logical paths in your app. For example, if the segue originated from a table view, the sender parameter would identify the table view cell that the user tapped. You could then use that information to set the data on the destination view controller.

## Parameters

- `segue`: The segue object containing information about the view controllers involved in the segue.
- `sender`: The object that initiated the segue. You might use this parameter to perform different actions based on which control (or other object) initiated the segue.

## See Also

### Performing segues
- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](./shouldperformsegue%28withidentifier,sender%29.md)
  Determines whether the segue with the specified identifier should be performed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/prepare(for:sender:))*