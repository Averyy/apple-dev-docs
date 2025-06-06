# delegate

**Framework**: UIKit  
**Kind**: property

The object that handles Writing Tools interactions for your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
weak var delegate: (any UIWritingToolsCoordinator.Delegate)? { get }
```

#### Discussion

Specify this object at initialization time when creating your `UIWritingToolsCoordinator` object. The object must adopt the [`UIWritingToolsCoordinator.Delegate`](uiwritingtoolscoordinator/delegate-swift.protocol.md) protocol, and be capable of modifying your view’s text storage and refreshing the view’s layout and appearance.

## See Also

- [UIWritingToolsCoordinator.Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.property)*