# UIWritingToolsCoordinator.State.inactive

**Framework**: UIKit  
**Kind**: case

A state that indicates Writing Tools isn’t currently performing any work on your view’s content.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case inactive
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

The coordinator starts in the `inactive` state, and transitions immediately to the [`UIWritingToolsCoordinator.State.noninteractive`](uiwritingtoolscoordinator/state-swift.enum/noninteractive.md) or [`UIWritingToolsCoordinator.State.interactiveResting`](uiwritingtoolscoordinator/state-swift.enum/interactiveresting.md) state when someone chooses an option from the Writing Tools UI. After the coordinator finishes incorporating any changes for the current operation, it returns to the `inactive` state and waits for the person to choose a different option or dismiss the Writing Tools UI.

## See Also

- [UIWritingToolsCoordinator.State.noninteractive](uiwritingtoolscoordinator/state-swift.enum/noninteractive.md)
  A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [UIWritingToolsCoordinator.State.interactiveResting](uiwritingtoolscoordinator/state-swift.enum/interactiveresting.md)
  A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [UIWritingToolsCoordinator.State.interactiveStreaming](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md)
  A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/inactive)*