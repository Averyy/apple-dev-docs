# id

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

An identifier for the turn.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let id: UUID
```

## Discussion

This identifier is stable across the round trip, and is how grading matches a transcript turn back to the turn that produced it. Two turns with the same utterance stay distinguishable.

## See Also

### Inspecting a user turn
- [let utterance: String](./utterance.md)
  The text a person says to Siri in this turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/userturn/id)*