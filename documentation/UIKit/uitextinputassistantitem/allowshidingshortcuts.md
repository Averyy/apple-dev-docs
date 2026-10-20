# allowsHidingShortcuts

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user can hide the shortcuts bar.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var allowsHidingShortcuts: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL allowsHidingShortcuts;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the user may hide the shortcuts bar when the keyboard is visible. When the value is [`false`](../../Swift/false.md), the shortcuts bar remains visible while the keyboard is visible. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring the shortcuts bar
- [var leadingBarButtonGroups: [UIBarButtonItemGroup]](./leadingbarbuttongroups.md)
  The array of button item groups to display before the typing suggestions.
- [var trailingBarButtonGroups: [UIBarButtonItemGroup]](./trailingbarbuttongroups.md)
  The array of button item groups to display after the typing suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/allowshidingshortcuts)*