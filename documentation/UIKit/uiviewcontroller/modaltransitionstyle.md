# modalTransitionStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The transition style to use when presenting the view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var modalTransitionStyle: UIModalTransitionStyle { get set }
```

```objc
@property (nonatomic, assign) UIModalTransitionStyle modalTransitionStyle;
```

## Discussion

This property determines how the view controller’s is animated onscreen when it is presented using the [`present(_:animated:completion:)`](./present%28_,animated,completion%29.md) method. To change the transition type, you must set this property before presenting the view controller. The default value for this property is [`UIModalTransitionStyle.coverVertical`](../uimodaltransitionstyle/coververtical.md).

For a list of possible transition styles, and their compatibility with the available presentation styles, see the [`UIModalTransitionStyle`](../uimodaltransitionstyle.md) constant descriptions.

## See Also

### Presenting a view controller
- [func show(UIViewController, sender: Any?)](./show%28_,sender%29.md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents a view controller in a secondary (or detail) context.
- [UIViewController.ShowDetailTargetDidChangeMessage](./showdetailtargetdidchangemessage.md)
- [func present(UIViewController, animated: Bool, completion: (() -> Void)?)](./present%28_,animated,completion%29.md)
  Presents a view controller modally.
- [func dismiss(animated: Bool, completion: (() -> Void)?)](./dismiss%28animated,completion%29.md)
  Dismisses the view controller that was presented modally by the view controller.
- [var modalPresentationStyle: UIModalPresentationStyle](./modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [enum UIModalPresentationStyle](../uimodalpresentationstyle.md)
  Modal presentation styles available when presenting view controllers.
- [enum UIModalTransitionStyle](../uimodaltransitionstyle.md)
  Transition styles available when presenting view controllers.
- [var isModalInPresentation: Bool](./ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var definesPresentationContext: Bool](./definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](./providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](./disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](./showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/modaltransitionstyle)*