# UIWritingToolsCoordinator.TextReplacementReason

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIWritingToolsCoordinatorTextReplacementReason : NSInteger;
```

#### Overview

During an operation, Writing Tools delivers replacement text to the delegate of the active [`UIWritingToolsCoordinator`](../uiwritingtoolscoordinator.md) object. Depending on the configured experience for your view, it delivers these changes as either interactive or noninteractive replacements. For interactive replacements, Writing Tools animates the change automatically and provides you with the information you need to perform any related animations.

## Topics

### Getting the reasons
- [UIWritingToolsCoordinator.TextReplacementReason.interactive](./textreplacementreason/interactive.md)
  An option to animate the replacement of text in your view.
- [UIWritingToolsCoordinator.TextReplacementReason.noninteractive](./textreplacementreason/noninteractive.md)
  An option to replace the text in your view without animating the change.
### Enumeration Cases
- [UIWritingToolsCoordinator.TextReplacementReason.accepted](./textreplacementreason/accepted.md)
  An option to replace the text in your view when a grammar suggestion is accepted.
- [UIWritingToolsCoordinator.TextReplacementReason.rejected](./textreplacementreason/rejected.md)
  An option to replace the text in your view when a grammar suggestion is rejected.
- [UIWritingToolsCoordinator.TextReplacementReason.temporary](./textreplacementreason/temporary.md)
  An option to replace the text in your view when a grammar suggestion is temporarily shown to preview the proposed change in the text.
### Initializers
- [init?(rawValue: Int)](./textreplacementreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the supporting types
- [UIWritingToolsCoordinator.ContextScope](./contextscope.md)
  Options that indicate how much of your content Writing Tools requested.
- [UIWritingToolsCoordinator.TextAnimation](./textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason)*