# items

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The items displayed on the toolbar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var items: [UIBarButtonItem]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<UIBarButtonItem *> * items;
```

## Discussion

The items, instances of [`UIBarButtonItem`](../uibarbuttonitem.md), that are visible on the toolbar in the order they appear in this array. Any changes to this property aren’t animated. Use the [`setItems(_:animated:)`](./setitems%28_,animated%29.md) method to animate changes.

The default value is `nil`.

## See Also

### Configuring toolbar items
- [func setItems([UIBarButtonItem]?, animated: Bool)](./setitems%28_,animated%29.md)
  Sets the items on the toolbar by animating the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/items)*