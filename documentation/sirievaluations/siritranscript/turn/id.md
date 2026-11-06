# id

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The identifier of the user turn that produced this turn.

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

Grading aligns by identity rather than by position, so a short or partial transcript cannot silently shift later observations into earlier turns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn/id)*