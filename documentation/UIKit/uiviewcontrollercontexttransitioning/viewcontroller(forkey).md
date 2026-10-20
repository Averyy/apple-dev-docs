# viewController(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a view controller involved in the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func viewController(forKey key: UITransitionContextViewControllerKey) -> UIViewController?
```

```objc
- (UIViewController *) viewControllerForKey:(UITransitionContextViewControllerKey) key;
```

#### Return Value

The view controller object for the specified key or `nil` if the view controller could not be found.

## Parameters

- `key`: The key identifying the view controller you want. For a list of possible keys, see `View Controller Transition Keys`.

## See Also

### Accessing the transition objects
- [var containerView: UIView](./containerview.md)
  The view that acts as the superview for the views involved in the transition.
- [func view(forKey: UITransitionContextViewKey) -> UIView?](./view%28forkey%29.md)
  Returns the specified view involved in the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/viewcontroller(forkey:))*