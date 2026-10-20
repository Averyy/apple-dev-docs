# UIScrollView.ContentInsetAdjustmentBehavior.scrollableAxes

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Adjust the insets only in the scrollable directions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case scrollableAxes
```

```c
UIScrollViewContentInsetAdjustmentScrollableAxes
```

#### Discussion

The top and bottom insets include the safe area inset values when the vertical content size is greater than the height of the scroll view itself. The top and bottom insets are also adjusted when the [`alwaysBounceVertical`](../alwaysbouncevertical.md) property is [`true`](../../../Swift/true.md). Similarly, the left and right insets include the safe area insets when the horizontal content size is greater than the width of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/scrollableaxes)*