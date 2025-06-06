# delegate

**Framework**: UIKit  
**Kind**: property

The search controller’s delegate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UISearchControllerDelegate)? { get set }
```

#### Discussion

Use the delegate object to receive notifications when the search results controller is presented and dismissed. You might use these notifications to customize the search interface or perform related actions.

## See Also

- [protocol UISearchControllerDelegate](uisearchcontrollerdelegate.md)
  A set of delegate methods for search controller objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/delegate)*