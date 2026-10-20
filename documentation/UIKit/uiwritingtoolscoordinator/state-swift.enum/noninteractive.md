# UIWritingToolsCoordinator.State.noninteractive

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.

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
UIWritingToolsCoordinatorStateNoninteractive
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](../../adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

Writing Tools transitions to this state when the coordinator uses the [`UIWritingToolsBehavior.limited`](../../uiwritingtoolsbehavior/limited.md) experience or when someone chooses an option that displays its results in the Writing Tools UI. When the person accepts the changes from the tool or dismisses the Writing Tools UI, the coordinator returns to the [`UIWritingToolsCoordinator.State.inactive`](./inactive.md) state. If the person discards the change and selects a tool with an interactive experience instead, the coordinator transitions to the [`UIWritingToolsCoordinator.State.interactiveResting`](./interactiveresting.md) state.

## See Also

### Getting the animation types
- [UIWritingToolsCoordinator.State.inactive](./inactive.md)
  A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [UIWritingToolsCoordinator.State.interactiveResting](./interactiveresting.md)
  A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [UIWritingToolsCoordinator.State.interactiveStreaming](./interactivestreaming.md)
  A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.enum/noninteractive)*