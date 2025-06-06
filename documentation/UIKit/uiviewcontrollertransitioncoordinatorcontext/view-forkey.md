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

## Parameters

- `key`: The key identifying the view you want. For a list of possible keys, see  .

## See Also

- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey:).md)
  Returns the view controllers involved in the transition.
- [var containerView: UIView](uiviewcontrollertransitioncoordinatorcontext/containerview.md)
  Returns the view in which the transition takes place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/view(forkey:))*