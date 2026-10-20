# isModalInPresentation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view controller enforces a modal behavior.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var isModalInPresentation: Bool { get set }
```

```objc
@property (nonatomic, getter=isModalInPresentation) BOOL modalInPresentation;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). When you set it to [`true`](../../Swift/true.md), UIKit ignores events outside the view controller’s bounds and prevents the interactive dismissal of the view controller while it is onscreen.

## See Also

### Related Documentation
- [Disabling the pull-down gesture for a sheet](../disabling-the-pull-down-gesture-for-a-sheet.md)
  Ensure a positive user experience when presenting a view controller as a sheet.
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
- [var modalTransitionStyle: UIModalTransitionStyle](./modaltransitionstyle.md)
  The transition style to use when presenting the view controller.
- [enum UIModalTransitionStyle](../uimodaltransitionstyle.md)
  Transition styles available when presenting view controllers.
- [var definesPresentationContext: Bool](./definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](./providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](./disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](./showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/ismodalinpresentation)*