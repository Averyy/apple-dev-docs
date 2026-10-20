# tab(forIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a tab with a matching identifier, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func tab(forIdentifier identifier: String) -> UITab?
```

```objc
- (UITab *) tabForIdentifier:(NSString *) identifier;
```

## See Also

### Accessing tabs
- [var children: [UITab]](./children.md)
  The tabs within a tab group.
- [var defaultChildIdentifier: String?](./defaultchildidentifier.md)
  The identifier for the default subitem.
- [var selectedChild: UITab?](./selectedchild.md)
  The currently selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/tab(foridentifier:))*