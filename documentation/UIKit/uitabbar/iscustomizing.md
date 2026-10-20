# isCustomizing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user is currently customizing the tab bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isCustomizing: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCustomizing) BOOL customizing;
```

## See Also

### Supporting user customization of tab bars
- [func beginCustomizingItems([UITabBarItem])](./begincustomizingitems%28_%29.md)
  Presents a standard interface that lets the user customize the contents of the tab bar.
- [func endCustomizing(animated: Bool) -> Bool](./endcustomizing%28animated%29.md)
  Dismisses the standard interface used to customize the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/iscustomizing)*