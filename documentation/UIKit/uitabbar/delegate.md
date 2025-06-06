# delegate

**Framework**: UIKit  
**Kind**: property

The tab bar’s delegate object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UITabBarDelegate)? { get set }
```

#### Discussion

Use the delegate to track the selection of tab bar items and to respond to the user customization of the tab bar. The default value of this property is `nil`.

For more information on how to implement the methods of this protocol, see [`UITabBarDelegate`](uitabbardelegate.md).

## See Also

- [protocol UITabBarDelegate](uitabbardelegate.md)
  The [`UITabBarDelegate`](uitabbardelegate.md) protocol defines optional methods for a delegate of a [`UITabBar`](uitabbar.md) object. The [`UITabBar`](uitabbar.md) class provides the ability for the user to reorder, remove, and add items to the tab bar; this process is referred to as customizing the tab bar. The tab bar delegate receives messages when customizing occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/delegate)*