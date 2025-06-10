# UIWritingToolsCoordinator.State.interactiveResting

**Framework**: UIKit  
**Kind**: case

A state that indicates Writing Tools is in the resting state for an inline editing experience.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case interactiveResting
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

When someone initially selects a tool with an interactive experience, the coordinator transitions briefly to this state and starts the operation. The coordinator transitions swiftly to the [`UIWritingToolsCoordinator.State.interactiveStreaming`](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md) state when it submits the request and delivers the results to your view. When it finishes delivering the results, it transitions back to the `interactiveResting` state and awaits further commands. If the person accepts the changes or dismisses the Writing Tools UI, the coordinator transitions from this state to the [`UIWritingToolsCoordinator.State.inactive`](uiwritingtoolscoordinator/state-swift.enum/inactive.md) state.

## See Also

- [UIWritingToolsCoordinator.State.inactive](uiwritingtoolscoordinator/state-swift.enum/inactive.md)
  A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinator.State.noninteractive](uiwritingtoolscoordinator/state-swift.enum/noninteractive.md)
  A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinator.State.interactiveStreaming](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md)
  A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/interactiveresting)*