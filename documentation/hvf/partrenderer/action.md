# PartRenderer.Action

**Framework**: hvf  
**Kind**: enum  
**Role**: Enumeration

Action requested by the render context after processing an instruction

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
enum Action
```

## Topics

### Enumeration Cases
- [PartRenderer.Action.continue](./action/continue.md)
  Continue rendering
- [PartRenderer.Action.skip](./action/skip.md)
  Skip this part (only in response to beginPart)
- [PartRenderer.Action.stop](./action/stop.md)
  Stop rendering

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/action)*