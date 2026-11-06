# SiriTranscript.IntentInvocation.Outcome

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

How a call Siri planned ended.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum Outcome
```

## Topics

### Identifying outcomes
- [SiriTranscript.IntentInvocation.Outcome.succeeded](./outcome-swift.enum/succeeded.md)
  The call ran and succeeded.
- [SiriTranscript.IntentInvocation.Outcome.failed](./outcome-swift.enum/failed.md)
  The call ran and failed, or could not find what it needed.
- [SiriTranscript.IntentInvocation.Outcome.needsInput](./outcome-swift.enum/needsinput.md)
  Siri stopped to ask the person for a missing value or to choose between candidates.
- [SiriTranscript.IntentInvocation.Outcome.awaitingConfirmation](./outcome-swift.enum/awaitingconfirmation.md)
  Siri chose the call and its arguments, and asked the person to confirm before running it.
- [SiriTranscript.IntentInvocation.Outcome.unknown](./outcome-swift.enum/unknown.md)
  Siri presented a result instead of a stop, such as a snippet or a search result.
- [SiriTranscript.IntentInvocation.Outcome.unreported](./outcome-swift.enum/unreported.md)
  No outcome was recorded for the call.
### Checking outcome state
- [var ran: Bool](./outcome-swift.enum/ran.md)
  Whether this counts as the call having run.
- [var committed: Bool](./outcome-swift.enum/committed.md)
  Whether Siri committed to the call.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Determining the outcome
- [let outcome: SiriTranscript.IntentInvocation.Outcome](./outcome-swift.property.md)
  How the call ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/outcome-swift.enum)*