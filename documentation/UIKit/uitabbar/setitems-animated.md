# setItems(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the items on the tab bar, optionally animating any changes into position.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setItems(_ items: [UITabBarItem]?, animated: Bool)
```

#### Discussion

Use this method to make changes to the currently visible items at runtime. Calling this method on a tab bar that is managed by a [`UITabBarController`](uitabbarcontroller.md) object raises an exception. When the tab bar is owned by a tab bar controller, use the tab bar controller’s methods to make changes to items.

## Parameters

- `items`: The array of   objects to display.
- `animated`: A Boolean indicating whether changes should be animated. Specify   to animate changes or   to display the new items without animations. When animations are enabled, the tab bar fades out removed items and fades in new items, adjusting the spacing between items as needed.

## See Also

- [var items: [UITabBarItem]?](uitabbar/items.md)
  The items displayed by the tab bar.
- [var selectedItem: UITabBarItem?](uitabbar/selecteditem.md)
  The currently selected item on the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/setitems(_:animated:))*