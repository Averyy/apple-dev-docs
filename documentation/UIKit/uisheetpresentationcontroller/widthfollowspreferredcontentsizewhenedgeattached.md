# widthFollowsPreferredContentSizeWhenEdgeAttached

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool { get set }
```

```objc
@property (nonatomic) BOOL widthFollowsPreferredContentSizeWhenEdgeAttached;
```

#### Discussion

The default value is [`false`](../../Swift/false.md), which means the sheet’s width equals the width of its container’s safe area. Set this value to [`true`](../../Swift/true.md) to use your view controller’s [`preferredContentSize`](../uiviewcontroller/preferredcontentsize.md) to determine the width of the sheet instead.

This property doesn’t have an effect when the sheet is in a compact-width and regular-height size class, or when [`prefersEdgeAttachedInCompactHeight`](./prefersedgeattachedincompactheight.md) is [`false`](../../Swift/false.md).

## See Also

### Managing the appearance
- [var prefersGrabberVisible: Bool](./prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersPageSizing: Bool](./preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var prefersEdgeAttachedInCompactHeight: Bool](./prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var preferredCornerRadius: CGFloat?](./preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached)*