# scrollViewDidEndScrollingAnimation(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when a scrolling animation in the scroll view concludes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView)
```

#### Discussion

The scroll view calls this method at the end of its implementations of the [`setContentOffset(_:animated:)`](uiscrollview/setcontentoffset(_:animated:).md) and [`scrollRectToVisible(_:animated:)`](uiscrollview/scrollrecttovisible(_:animated:).md) methods, but only if animations are requested.

## Parameters

- `scrollView`: The scroll-view object that’s performing the scrolling animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidendscrollinganimation(_:))*