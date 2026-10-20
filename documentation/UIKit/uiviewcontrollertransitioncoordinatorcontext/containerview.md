# containerView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the view in which the transition takes place.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var containerView: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * containerView;
```

#### Return Value

The container view for the transition animation.

#### Discussion

The container view acts as the host view for any animations between the transitioning view controllers. When animating your own custom views, add them to the container view if you want them to interoperate with the view controllers’ views.

## See Also

### Getting the views and view controllers
- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](./viewcontroller%28forkey%29.md)
  Returns the view controllers involved in the transition.
- [func view(forKey: UITransitionContextViewKey) -> UIView?](./view%28forkey%29.md)
  Returns the specified view involved in the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/containerview)*