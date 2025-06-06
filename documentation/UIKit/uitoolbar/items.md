# items

**Framework**: UIKit  
**Kind**: property

The items displayed on the toolbar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var items: [UIBarButtonItem]? { get set }
```

#### Discussion

The items, instances of [`UIBarButtonItem`](uibarbuttonitem.md), that are visible on the toolbar in the order they appear in this array. Any changes to this property aren’t animated. Use the [`setItems(_:animated:)`](uitoolbar/setitems(_:animated:).md) method to animate changes.

The default value is `nil`.

## See Also

- [func setItems([UIBarButtonItem]?, animated: Bool)](uitoolbar/setitems(_:animated:).md)
  Sets the items on the toolbar by animating the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/items)*