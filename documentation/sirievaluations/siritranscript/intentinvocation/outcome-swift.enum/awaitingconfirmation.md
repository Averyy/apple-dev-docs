# SiriTranscript.IntentInvocation.Outcome.awaitingConfirmation

**Framework**: Siri Evaluations  
**Kind**: case  
**Role**: Case

Siri chose the call and its arguments, and asked the person to confirm before running it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
case awaitingConfirmation
```

## See Also

### Identifying outcomes
- [SiriTranscript.IntentInvocation.Outcome.succeeded](./succeeded.md)
  The call ran and succeeded.
- [SiriTranscript.IntentInvocation.Outcome.failed](./failed.md)
  Siri called it and it failed: its tool threw, or it ended in another error. It doesn’t count as having run.
- [SiriTranscript.IntentInvocation.Outcome.needsInput](./needsinput.md)
  Siri stopped to ask the person for a missing value or to choose between candidates, or the person cancelled the call when asked.
- [SiriTranscript.IntentInvocation.Outcome.unknown](./unknown.md)
  Siri presented a result instead of a stop, such as a snippet or a search result.
- [SiriTranscript.IntentInvocation.Outcome.unreported](./unreported.md)
  No outcome was recorded for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/outcome-swift.enum/awaitingconfirmation)*