# view(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the specified view involved in the transition.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func view(forKey key: UITransitionContextViewKey) -> UIView?
```

```objc
- (UIView *) viewForKey:(UITransitionContextViewKey) key;
```

## Return Value

The view object for the specified key or `nil` if the view could not be found.

## Parameters

- `key`: The key identifying the view you want. For a list of possible keys, see [`UITransitionContextViewKey`](../uitransitioncontextviewkey.md).

## See Also

### Getting the views and view controllers
- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](./viewcontroller%28forkey%29.md)
  Returns the view controllers involved in the transition.
- [var containerView: UIView](./containerview.md)
  Returns the view in which the transition takes place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/view(forkey:))*