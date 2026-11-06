# turns

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The turns the run reached, in conversation order.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let turns: [SiriTranscript.Turn]
```

## Discussion

A turn the run never reached is absent. A turn that got no reply is still listed, with an empty response.

## See Also

### Inspecting a transcript
- [func turn(for: UUID) -> SiriTranscript.Turn?](./turn%28for%29.md)
  Returns the turn produced by the scenario turn with this identity, if it ran.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turns)*