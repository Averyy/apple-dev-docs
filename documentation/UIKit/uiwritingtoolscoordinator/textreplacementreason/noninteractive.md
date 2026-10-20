# UIWritingToolsCoordinator.TextReplacementReason.noninteractive

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An option to replace the text in your view without animating the change.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case noninteractive
```

```c
UIWritingToolsCoordinatorTextReplacementReasonNoninteractive
```

#### Discussion

When Writing Tools requests a noninteractive change in your delegate’s `UIWritingToolsCoordinator/Delegate/writingToolsCoordinator(_:replaceRange:inContext:proposedText:reason:animationParameters:completion:)` method, update your view’s text storage without animating the change.

## See Also

### Getting the reasons
- [UIWritingToolsCoordinator.TextReplacementReason.interactive](./interactive.md)
  An option to animate the replacement of text in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/noninteractive)*