# contentLayoutGuide

**Framework**: UIKit  
**Kind**: property

The layout guide based on the untranslated content rectangle of the scroll view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentLayoutGuide: UILayoutGuide { get }
```

#### Discussion

Use this layout guide when you want to create Auto Layout constraints related to the content area of a scroll view.

## See Also

- [var frameLayoutGuide: UILayoutGuide](uiscrollview/framelayoutguide.md)
  The layout guide based on the untransformed frame rectangle of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentlayoutguide)*