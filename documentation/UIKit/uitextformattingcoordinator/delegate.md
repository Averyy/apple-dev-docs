# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the text-formatting coordinator.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UITextFormattingCoordinatorDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UITextFormattingCoordinatorDelegate> delegate;
```

## See Also

### Applying Updated Text Attributes
- [protocol UITextFormattingCoordinatorDelegate](../uitextformattingcoordinatordelegate.md)
  The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingcoordinator/delegate)*