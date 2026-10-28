# endCustomizing(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the standard interface used to customize the tab bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func endCustomizing(animated: Bool) -> Bool
```

```objc
- (BOOL) endCustomizingAnimated:(BOOL) animated;
```

## Return Value

[`true`](../../Swift/true.md) if items on the tab bar changed or [`false`](../../Swift/false.md) if they did not.

## Discussion

You rarely need to call this method. Typically, the user dismisses the modal view by tapping the built-in Done button in the interface. However, you might call this method to cancel the customization process because of changes to other parts of your interface.

## Parameters

- `animated`: If [`true`](../../Swift/true.md), animate the dismissal of the interface.

## See Also

### Supporting user customization of tab bars
- [func beginCustomizingItems([UITabBarItem])](./begincustomizingitems%28_%29.md)
  Presents a standard interface that lets the user customize the contents of the tab bar.
- [var isCustomizing: Bool](./iscustomizing.md)
  A Boolean value indicating whether the user is currently customizing the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/endcustomizing(animated:))*