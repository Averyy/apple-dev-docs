# delegate

**Framework**: UIKit  
**Kind**: property

The delegate you use to manage changes to a split view interface.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UISplitViewControllerDelegate)? { get set }
```

#### Discussion

The split view controller uses its delegate to manage showing and hiding related view controllers. For more information about the methods you can implement in your delegate, see [`UISplitViewControllerDelegate`](uisplitviewcontrollerdelegate.md).

## See Also

- [protocol UISplitViewControllerDelegate](uisplitviewcontrollerdelegate.md)
  The methods adopted by the object you use to manage changes to a split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/delegate)*