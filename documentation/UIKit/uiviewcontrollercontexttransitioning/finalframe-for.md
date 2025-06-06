# finalFrame(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the ending frame rectangle for the specified view controller’s view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func finalFrame(for vc: UIViewController) -> CGRect
```

#### Return Value

The frame rectangle for the view or [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) if the frame rectangle is not known or the view is not visible.

#### Discussion

The rectangle returned by this method represents the size of the corresponding view at the end of the transition. For the view being covered during the presentation, the value returned by this method might be [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) but it might also be a valid frame rectangle.

## Parameters

- `vc`: The view controller whose frame rectangle you want.

## See Also

- [func initialFrame(for: UIViewController) -> CGRect](uiviewcontrollercontexttransitioning/initialframe(for:).md)
  Returns the starting frame rectangle for the specified view controller’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/finalframe(for:))*