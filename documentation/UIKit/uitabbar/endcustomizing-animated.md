# endCustomizing(animated:)

**Framework**: UIKit  
**Kind**: method

Dismisses the standard interface used to customize the tab bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func endCustomizing(animated: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if items on the tab bar changed or [`false`](https://developer.apple.com/documentation/swift/false) if they did not.

#### Discussion

You rarely need to call this method. Typically, the user dismisses the modal view by tapping the built-in Done button in the interface. However, you might call this method to cancel the customization process because of changes to other parts of your interface.

## Parameters

- `animated`: If  , animate the dismissal of the interface.

## See Also

- [func beginCustomizingItems([UITabBarItem])](uitabbar/begincustomizingitems(_:).md)
  Presents a standard interface that lets the user customize the contents of the tab bar.
- [var isCustomizing: Bool](uitabbar/iscustomizing.md)
  A Boolean value indicating whether the user is currently customizing the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/endcustomizing(animated:))*