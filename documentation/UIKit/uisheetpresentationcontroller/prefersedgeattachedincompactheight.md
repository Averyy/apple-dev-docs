# prefersEdgeAttachedInCompactHeight

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var prefersEdgeAttachedInCompactHeight: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false), which means the sheet defaults to a full screen appearance at compact height. Set this value to [`true`](https://developer.apple.com/documentation/swift/true) to use an alternate appearance in a compact-height size class, causing the sheet to only attach to the screen on its bottom edge.

## See Also

- [var prefersGrabberVisible: Bool](uisheetpresentationcontroller/prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersPageSizing: Bool](uisheetpresentationcontroller/preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [var preferredCornerRadius: CGFloat?](uisheetpresentationcontroller/preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersedgeattachedincompactheight)*