# delegate

**Framework**: UIKit  
**Kind**: property

The delegate of the text-formatting coordinator.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UITextFormattingCoordinatorDelegate)? { get set }
```

## See Also

- [protocol UITextFormattingCoordinatorDelegate](uitextformattingcoordinatordelegate.md)
  The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingcoordinator/delegate)*