# prefersEdgeAttachedInCompactHeight

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var prefersEdgeAttachedInCompactHeight: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersEdgeAttachedInCompactHeight;
```

#### Discussion

The default value is [`false`](../../Swift/false.md), which means the sheet defaults to a full screen appearance at compact height. Set this value to [`true`](../../Swift/true.md) to use an alternate appearance in a compact-height size class, causing the sheet to only attach to the screen on its bottom edge.

## See Also

### Managing the appearance
- [var prefersGrabberVisible: Bool](./prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersPageSizing: Bool](./preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](./widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [var preferredCornerRadius: CGFloat?](./preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersedgeattachedincompactheight)*