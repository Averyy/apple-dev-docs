# UIWritingToolsCoordinator.ContextScope

**Framework**: UIKit  
**Kind**: enum

Options that indicate how much of your content Writing Tools requested.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
enum ContextScope
```

#### Overview

At the start of any Writing Tools interaction, you provide the text for the system to evaluate from your [`UIWritingToolsCoordinator.Delegate`](uiwritingtoolscoordinator/delegate-swift.protocol.md) object. The request for your content comes with a scope constant that indicates how much of your view’s text to provide.

## Topics

### Getting the scope
- [UIWritingToolsCoordinator.ContextScope.userSelection](uiwritingtoolscoordinator/contextscope/userselection.md)
  An option to provide only the view’s currently selected text.
- [UIWritingToolsCoordinator.ContextScope.fullDocument](uiwritingtoolscoordinator/contextscope/fulldocument.md)
  An option to provide all of your view’s text.
- [UIWritingToolsCoordinator.ContextScope.visibleArea](uiwritingtoolscoordinator/contextscope/visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.
### Initializers
- [init?(rawValue: Int)](uiwritingtoolscoordinator/contextscope/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIWritingToolsCoordinator.TextReplacementReason](uiwritingtoolscoordinator/textreplacementreason.md)
  Options that indicate whether Writing Tools is animating changes to your view’s text.
- [UIWritingToolsCoordinator.TextAnimation](uiwritingtoolscoordinator/textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope)*