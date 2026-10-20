# children

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tabs within a tab group.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var children: [UITab] { get set }
```

```objc
@property (nonatomic, copy) NSArray<UITab *> * children;
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

## See Also

### Accessing tabs
- [func tab(forIdentifier: String) -> UITab?](./tab%28foridentifier%29.md)
  Returns a tab with a matching identifier, if any.
- [var defaultChildIdentifier: String?](./defaultchildidentifier.md)
  The identifier for the default subitem.
- [var selectedChild: UITab?](./selectedchild.md)
  The currently selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/children)*