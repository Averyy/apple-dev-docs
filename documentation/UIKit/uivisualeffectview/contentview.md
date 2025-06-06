# contentView

**Framework**: UIKit  
**Kind**: property

A view object that can have a visual effect view added to it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentView: UIView { get }
```

#### Discussion

Add subviews to the [`contentView`](uivisualeffectview/contentview.md) and not to [`UIVisualEffectView`](uivisualeffectview.md) directly.

## See Also

- [var effect: UIVisualEffect?](uivisualeffectview/effect.md)
  The visual effect provided by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivisualeffectview/contentview)*