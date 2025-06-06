# UIWritingToolsCoordinator.TextAnimation

**Framework**: UIKit  
**Kind**: enum

The types of animations that Writing Tools performs during an interactive update of your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
enum TextAnimation
```

#### Overview

Use the `UIWritingToolsCoordinator/TextAnimation` constants to determine the type of animation that is occurring. During an interactive change to your view, Writing Tools creates animations to provide feedback about what’s happening. During the setup for each animation, Writing Tools reports the type of animation to the coordinator’s delegate, so that you can perform additional actions related to that animation. For example, during an insertion animation, you might animate changes to other views in your interface.

## Topics

### Getting the animation types
- [UIWritingToolsCoordinator.TextAnimation.anticipate](uiwritingtoolscoordinator/textanimation/anticipate.md)
  The animation that Writing Tools performs when waiting to receive results from the large language model.
- [UIWritingToolsCoordinator.TextAnimation.insert](uiwritingtoolscoordinator/textanimation/insert.md)
  The animation that Writing Tools performs when inserting text into your view.
- [UIWritingToolsCoordinator.TextAnimation.remove](uiwritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.
### Initializers
- [init?(rawValue: Int)](uiwritingtoolscoordinator/textanimation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIWritingToolsCoordinator.ContextScope](uiwritingtoolscoordinator/contextscope.md)
  Options that indicate how much of your content Writing Tools requested.
- [UIWritingToolsCoordinator.TextReplacementReason](uiwritingtoolscoordinator/textreplacementreason.md)
  Options that indicate whether Writing Tools is animating changes to your view’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation)*