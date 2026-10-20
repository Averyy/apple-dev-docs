# initialFrame(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the starting frame rectangle for the specified view controller’s view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func initialFrame(for vc: UIViewController) -> CGRect
```

```objc
- (CGRect) initialFrameForViewController:(UIViewController *) vc;
```

#### Return Value

The frame rectangle for the view or [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if the frame rectangle is not known or the view is not visible.

#### Discussion

The rectangle returned by this method represents the size of the corresponding view at the beginning of the transition. For the view controller that is already onscreen, this rectangle typically matches the frame rectangle of the container view. For the view controller being presented, the value returned by this method is typically [`CGRectZero`](../../CoreGraphics/cgrectzero.md) because the view is not yet on screen.

## Parameters

- `vc`: The view controller whose frame rectangle you want.

## See Also

### Getting the transition frame rectangles
- [func finalFrame(for: UIViewController) -> CGRect](./finalframe%28for%29.md)
  Returns the ending frame rectangle for the specified view controller’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/initialframe(for:))*