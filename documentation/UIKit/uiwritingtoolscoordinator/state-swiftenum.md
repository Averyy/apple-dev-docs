# UIWritingToolsCoordinator.State

**Framework**: UIKit  
**Kind**: enum

The states that indicate the current activity, if any, Writing Tools is performing in your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
enum State
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Overview

Making changes to your view requires several different levels of interaction. Initially, Writing Tools displays its UI and collects information about what the person wants to do. When the person selects an operation, Writing Tools sends the relevant details to a large language model (LLM) and processes the results. It then works with the custom view to integrate any changes into the view’s text storage. During each of these activities, the coordinator reflects what’s happening in its [`state`](uiwritingtoolscoordinator/state-swift.property.md) property. You can use the current state as a guide to making decisions in other parts of your view.

## Topics

### Getting the animation types
- [UIWritingToolsCoordinator.State.inactive](uiwritingtoolscoordinator/state-swift.enum/inactive.md)
  A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinator.State.noninteractive](uiwritingtoolscoordinator/state-swift.enum/noninteractive.md)
  A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinator.State.interactiveResting](uiwritingtoolscoordinator/state-swift.enum/interactiveresting.md)
  A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [UIWritingToolsCoordinator.State.interactiveStreaming](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md)
  A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.
### Initializers
- [init?(rawValue: Int)](uiwritingtoolscoordinator/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func stopWritingTools()](uiwritingtoolscoordinator/stopwritingtools.md)
  Stops the current Writing Tools operation and dismisses the system UI.
- [var state: UIWritingToolsCoordinator.State](uiwritingtoolscoordinator/state-swift.property.md)
  The current level of Writing Tools activity in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum)*