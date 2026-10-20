# selectedChild

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The currently selected tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var selectedChild: UITab? { get set }
```

```objc
@property (nonatomic, strong, nullable) UITab * selectedChild;
```

## See Also

### Accessing tabs
- [var children: [UITab]](./children.md)
  The tabs within a tab group.
- [func tab(forIdentifier: String) -> UITab?](./tab%28foridentifier%29.md)
  Returns a tab with a matching identifier, if any.
- [var defaultChildIdentifier: String?](./defaultchildidentifier.md)
  The identifier for the default subitem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/selectedchild)*