# UIWritingToolsCoordinator.TextReplacementReason.interactive

**Framework**: UIKit  
**Kind**: case

An option to animate the replacement of text in your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case interactive
```

#### Discussion

When Writing Tools requests an interactive change in your delegate’s `UIWritingToolsCoordinator/Delegate/writingToolsCoordinator(_:replaceRange:inContext:proposedText:reason:animationParameters:completion:)` method, it passes a valid set of animation parameters to that method. Update your view’s text storage and use the provided [`UIWritingToolsCoordinator.AnimationParameters`](uiwritingtoolscoordinator/animationparameters.md) type to create any view-specific animations you need to support the animated replacement of the text.

## See Also

- [UIWritingToolsCoordinator.TextReplacementReason.noninteractive](uiwritingtoolscoordinator/textreplacementreason/noninteractive.md)
  An option to replace the text in your view without animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/interactive)*