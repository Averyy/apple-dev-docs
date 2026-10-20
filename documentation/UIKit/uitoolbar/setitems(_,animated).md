# setItems(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the items on the toolbar by animating the changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setItems(_ items: [UIBarButtonItem]?, animated: Bool)
```

```objc
- (void) setItems:(NSArray<UIBarButtonItem *> *) items animated:(BOOL) animated;
```

#### Discussion

If `animated` is [`true`](../../Swift/true.md), the changes are dissolved or the reordering is animated—for example, removed items fade out and new items fade in. This method also adjusts the spacing between items.

## Parameters

- `items`: The items to display on the toolbar.
- `animated`: A Boolean value if set to [`true`](../../Swift/true.md) animates the transition to the items; otherwise, does not.

## See Also

### Configuring toolbar items
- [var items: [UIBarButtonItem]?](./items.md)
  The items displayed on the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/setitems(_:animated:))*