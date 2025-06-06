# setItems(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the items on the toolbar by animating the changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setItems(_ items: [UIBarButtonItem]?, animated: Bool)
```

#### Discussion

If `animated` is [`true`](https://developer.apple.com/documentation/swift/true), the changes are dissolved or the reordering is animated—for example, removed items fade out and new items fade in. This method also adjusts the spacing between items.

## Parameters

- `items`: The items to display on the toolbar.
- `animated`: A Boolean value if set to   animates the transition to the items; otherwise, does not.

## See Also

- [var items: [UIBarButtonItem]?](uitoolbar/items.md)
  The items displayed on the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/setitems(_:animated:))*