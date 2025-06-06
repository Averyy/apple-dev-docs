# view(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the specified view involved in the transition.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func view(forKey key: UITransitionContextViewKey) -> UIView?
```

#### Return Value

The view object for the specified key or `nil` if the view could not be found.

#### Discussion

The view returned by this method may or may not be the root view of the corresponding view controller. A situation where the views may not be the same is when a system-provided presentation controller installs another view underneath the presented view controller’s view.

## Parameters

- `key`: The key identifying the view you want. For a list of possible keys, see  .

## See Also

- [var containerView: UIView](uiviewcontrollercontexttransitioning/containerview.md)
  The view that acts as the superview for the views involved in the transition.
- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](uiviewcontrollercontexttransitioning/viewcontroller(forkey:).md)
  Returns a view controller involved in the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/view(forkey:))*