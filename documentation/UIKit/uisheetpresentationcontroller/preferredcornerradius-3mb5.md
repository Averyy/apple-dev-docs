# preferredCornerRadius

**Framework**: UIKit  
**Kind**: property

The corner radius that the sheet attempts to present with.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@preconcurrency var preferredCornerRadius: CGFloat? { get set }
```

#### Discussion

The default value is `nil`. This property only has an effect when the sheet is at the front of its sheet stack.

## See Also

- [var prefersGrabberVisible: Bool](uisheetpresentationcontroller/prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersPageSizing: Bool](uisheetpresentationcontroller/preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var prefersEdgeAttachedInCompactHeight: Bool](uisheetpresentationcontroller/prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferredcornerradius-3mb5)*