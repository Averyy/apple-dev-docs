# delegate

**Framework**: UIKit  
**Kind**: property

The tab bar controller’s delegate object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UITabBarControllerDelegate)? { get set }
```

#### Discussion

You can use the delegate object to track changes to the items in the tab bar and to monitor the selection of tabs. The delegate object you provide should conform to the [`UITabBarControllerDelegate`](uitabbarcontrollerdelegate.md) protocol. The default value for this property is `nil`.

## See Also

- [protocol UITabBarControllerDelegate](uitabbarcontrollerdelegate.md)
  A set of methods you implement to customize the behavior of a tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/delegate)*