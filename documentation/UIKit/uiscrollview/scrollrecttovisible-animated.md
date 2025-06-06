# scrollRectToVisible(_:animated:)

**Framework**: UIKit  
**Kind**: method

Scrolls a specific area of the content so that it’s visible in the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func scrollRectToVisible(_ rect: CGRect, animated: Bool)
```

#### Discussion

This method scrolls the content view so that the area defined by `rect` is just visible inside the scroll view. If the area is already visible, the method does nothing.

## Parameters

- `rect`: A rectangle defining an area of the content view. The rectangle should be in the coordinate space of the scroll view.
- `animated`:   if the scrolling should be animated,   if it should be immediate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/scrollrecttovisible(_:animated:))*