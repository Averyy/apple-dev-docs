# SiriTranscript.IntentInvocation.Outcome.unreported

**Framework**: Siri Evaluations  
**Kind**: case  
**Role**: Case

No outcome was recorded for the call.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
case unreported
```

## Discussion

It satisfies no `Calls`, and `Calls(.disallowed)` treats it as committed.

## See Also

### Identifying outcomes
- [SiriTranscript.IntentInvocation.Outcome.succeeded](./succeeded.md)
  The call ran and succeeded.
- [SiriTranscript.IntentInvocation.Outcome.failed](./failed.md)
  The call ran and failed, or could not find what it needed.
- [SiriTranscript.IntentInvocation.Outcome.needsInput](./needsinput.md)
  Siri stopped to ask the person for a missing value or to choose between candidates.
- [SiriTranscript.IntentInvocation.Outcome.awaitingConfirmation](./awaitingconfirmation.md)
  Siri chose the call and its arguments, and asked the person to confirm before running it.
- [SiriTranscript.IntentInvocation.Outcome.unknown](./unknown.md)
  Siri presented a result instead of a stop, such as a snippet or a search result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/outcome-swift.enum/unreported)*