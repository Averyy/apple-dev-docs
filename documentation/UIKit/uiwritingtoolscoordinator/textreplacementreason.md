# UIWritingToolsCoordinator.TextReplacementReason

**Framework**: UIKit  
**Kind**: enum

Options that indicate whether Writing Tools is animating changes to your view’s text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
enum TextReplacementReason
```

#### Overview

During an operation, Writing Tools delivers replacement text to the delegate of the active [`UIWritingToolsCoordinator`](uiwritingtoolscoordinator.md) object. Depending on the configured experience for your view, it delivers these changes as either interactive or noninteractive replacements. For interactive replacements, Writing Tools animates the change automatically and provides you with the information you need to perform any related animations.

## Topics

### Getting the reasons
- [UIWritingToolsCoordinator.TextReplacementReason.interactive](uiwritingtoolscoordinator/textreplacementreason/interactive.md)
  An option to animate the replacement of text in your view.
- [UIWritingToolsCoordinator.TextReplacementReason.noninteractive](uiwritingtoolscoordinator/textreplacementreason/noninteractive.md)
  An option to replace the text in your view without animating the change.
### Initializers
- [init?(rawValue: Int)](uiwritingtoolscoordinator/textreplacementreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIWritingToolsCoordinator.ContextScope](uiwritingtoolscoordinator/contextscope.md)
  Options that indicate how much of your content Writing Tools requested.
- [UIWritingToolsCoordinator.TextAnimation](uiwritingtoolscoordinator/textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason)*