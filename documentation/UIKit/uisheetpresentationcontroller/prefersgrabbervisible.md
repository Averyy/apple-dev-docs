# prefersGrabberVisible

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the sheet shows a grabber at the top.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
var prefersGrabberVisible: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false), which means the sheet doesn’t show a grabber. A  is a visual affordance that indicates that a sheet is resizable. Showing a grabber may be useful when it isn’t apparent that a sheet can resize or when the sheet can’t dismiss interactively.

Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) for the system to draw a grabber in the standard system-defined location. The system automatically hides the grabber at appropriate times, like when the sheet is full screen in a compact-height size class or when another sheet presents on top of it.

## See Also

- [var prefersPageSizing: Bool](uisheetpresentationcontroller/preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var prefersEdgeAttachedInCompactHeight: Bool](uisheetpresentationcontroller/prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [var preferredCornerRadius: CGFloat?](uisheetpresentationcontroller/preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible)*