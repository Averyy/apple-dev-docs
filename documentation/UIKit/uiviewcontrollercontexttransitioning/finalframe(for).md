# finalFrame(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the ending frame rectangle for the specified view controller’s view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func finalFrame(for vc: UIViewController) -> CGRect
```

```objc
- (CGRect) finalFrameForViewController:(UIViewController *) vc;
```

## Return Value

The frame rectangle for the view or [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if the frame rectangle is not known or the view is not visible.

## Discussion

The rectangle returned by this method represents the size of the corresponding view at the end of the transition. For the view being covered during the presentation, the value returned by this method might be [`CGRectZero`](../../CoreGraphics/cgrectzero.md) but it might also be a valid frame rectangle.

## Parameters

- `vc`: The view controller whose frame rectangle you want.

## See Also

### Getting the transition frame rectangles
- [func initialFrame(for: UIViewController) -> CGRect](./initialframe%28for%29.md)
  Returns the starting frame rectangle for the specified view controller’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/finalframe(for:))*