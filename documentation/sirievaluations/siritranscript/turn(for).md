# turn(for:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Instance Method

Returns the turn produced by the scenario turn with this identity, if it ran.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
func turn(for id: UUID) -> SiriTranscript.Turn?
```

## Discussion

Lookup by identity rather than index: a scenario that was interrupted has fewer transcript turns than scenario turns, and positional lookup would grade turn three’s expectations against turn two’s observations.

## See Also

### Inspecting a transcript
- [let turns: [SiriTranscript.Turn]](./turns.md)
  The turns the run reached, in conversation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn(for:))*