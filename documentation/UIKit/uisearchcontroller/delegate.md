# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The search controller’s delegate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UISearchControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UISearchControllerDelegate> delegate;
```

#### Discussion

Use the delegate object to receive notifications when the search results controller is presented and dismissed. You might use these notifications to customize the search interface or perform related actions.

## See Also

### Responding to presentation and dismissal
- [protocol UISearchControllerDelegate](../uisearchcontrollerdelegate.md)
  A set of delegate methods for search controller objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/delegate)*