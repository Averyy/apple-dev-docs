# viewController(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the view controllers involved in the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewController(forKey key: UITransitionContextViewControllerKey) -> UIViewController?
```

#### Return Value

The view controller associated with the key.

#### Discussion

The view controller associated with the [`from`](uitransitioncontextviewcontrollerkey/from.md) key corresponds to the view controller that’s already onscreen. The view controller associated with the [`to`](uitransitioncontextviewcontrollerkey/to.md) key corresponds to the view controller that’s to be animated onscreen.

## Parameters

- `key`: The key indicating which view controller you want. For a list of possible values, see  .

## See Also

- [func view(forKey: UITransitionContextViewKey) -> UIView?](uiviewcontrollertransitioncoordinatorcontext/view(forkey:).md)
  Returns the specified view involved in the transition.
- [var containerView: UIView](uiviewcontrollertransitioncoordinatorcontext/containerview.md)
  Returns the view in which the transition takes place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey:))*