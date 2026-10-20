# defaultChildIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The identifier for the default subitem.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var defaultChildIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * defaultChildIdentifier;
```

## See Also

### Accessing tabs
- [var children: [UITab]](./children.md)
  The tabs within a tab group.
- [func tab(forIdentifier: String) -> UITab?](./tab%28foridentifier%29.md)
  Returns a tab with a matching identifier, if any.
- [var selectedChild: UITab?](./selectedchild.md)
  The currently selected tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/defaultchildidentifier)*