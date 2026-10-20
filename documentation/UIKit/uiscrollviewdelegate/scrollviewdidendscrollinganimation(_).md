# scrollViewDidEndScrollingAnimation(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when a scrolling animation in the scroll view concludes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView)
```

```objc
- (void) scrollViewDidEndScrollingAnimation:(UIScrollView *) scrollView;
```

#### Discussion

The scroll view calls this method at the end of its implementations of the [`setContentOffset(_:animated:)`](../uiscrollview/setcontentoffset%28_,animated%29.md) and [`scrollRectToVisible(_:animated:)`](../uiscrollview/scrollrecttovisible%28_,animated%29.md) methods, but only if animations are requested.

## Parameters

- `scrollView`: The scroll-view object that’s performing the scrolling animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidendscrollinganimation(_:))*