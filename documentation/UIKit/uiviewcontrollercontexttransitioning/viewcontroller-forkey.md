# viewController(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a view controller involved in the transition.

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

The view controller object for the specified key or `nil` if the view controller could not be found.

## Parameters

- `key`: The key identifying the view controller you want. For a list of possible keys, see  .

## See Also

- [var containerView: UIView](uiviewcontrollercontexttransitioning/containerview.md)
  The view that acts as the superview for the views involved in the transition.
- [func view(forKey: UITransitionContextViewKey) -> UIView?](uiviewcontrollercontexttransitioning/view(forkey:).md)
  Returns the specified view involved in the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/viewcontroller(forkey:))*