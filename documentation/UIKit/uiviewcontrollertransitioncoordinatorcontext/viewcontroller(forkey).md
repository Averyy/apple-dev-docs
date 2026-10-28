# viewController(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the view controllers involved in the transition.

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

## Return Value

The view controller associated with the key.

## Discussion

The view controller associated with the [`from`](../uitransitioncontextviewcontrollerkey/from.md) key corresponds to the view controller that’s already onscreen. The view controller associated with the [`to`](../uitransitioncontextviewcontrollerkey/to.md) key corresponds to the view controller that’s to be animated onscreen.

## Parameters

- `key`: The key indicating which view controller you want. For a list of possible values, see [`UITransitionContextViewControllerKey`](../uitransitioncontextviewcontrollerkey.md).

## See Also

### Getting the views and view controllers
- [func view(forKey: UITransitionContextViewKey) -> UIView?](./view%28forkey%29.md)
  Returns the specified view involved in the transition.
- [var containerView: UIView](./containerview.md)
  Returns the view in which the transition takes place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey:))*