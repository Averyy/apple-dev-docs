# UITextFormattingCoordinatorDelegate

**Framework**: UIKit  
**Kind**: protocol

The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextFormattingCoordinatorDelegate : NSObjectProtocol
```

## Topics

### Updating Text Attributes
- [func updateTextAttributes(conversionHandler: ([NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any])](uitextformattingcoordinatordelegate/updatetextattributes(conversionhandler:).md)
  Applies the current font panel settings to the selected text.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UITextFormattingCoordinatorDelegate)?](uitextformattingcoordinator/delegate.md)
  The delegate of the text-formatting coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingcoordinatordelegate)*