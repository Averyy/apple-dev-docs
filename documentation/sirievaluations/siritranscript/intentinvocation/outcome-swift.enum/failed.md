# SiriTranscript.IntentInvocation.Outcome.failed

**Framework**: Siri Evaluations  
**Kind**: case  
**Role**: Case

The call ran and failed, or could not find what it needed.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
case failed
```

## Discussion

An outcome this version of the framework doesn’t recognize, which only a newer daemon can report, is also reported as failed.

## See Also

### Identifying outcomes
- [SiriTranscript.IntentInvocation.Outcome.succeeded](./succeeded.md)
  The call ran and succeeded.
- [SiriTranscript.IntentInvocation.Outcome.needsInput](./needsinput.md)
  Siri stopped to ask the person for a missing value or to choose between candidates.
- [SiriTranscript.IntentInvocation.Outcome.awaitingConfirmation](./awaitingconfirmation.md)
  Siri chose the call and its arguments, and asked the person to confirm before running it.
- [SiriTranscript.IntentInvocation.Outcome.unknown](./unknown.md)
  Siri presented a result instead of a stop, such as a snippet or a search result.
- [SiriTranscript.IntentInvocation.Outcome.unreported](./unreported.md)
  No outcome was recorded for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/outcome-swift.enum/failed)*