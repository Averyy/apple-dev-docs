# response

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The reply Siri concluded the turn with, including an apology or a timeout message.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let response: SiriTranscript.Observation<String>
```

## See Also

### Inspecting what Siri does
- [let intentInvocations: [SiriTranscript.Observation<SiriTranscript.IntentInvocation>]](./intentinvocations.md)
  The intents Siri invoked during the turn, with the arguments it bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn/response)*