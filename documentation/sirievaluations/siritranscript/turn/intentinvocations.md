# intentInvocations

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The intents Siri invoked during the turn, with the arguments it bound.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let intentInvocations: [SiriTranscript.Observation<SiriTranscript.IntentInvocation>]
```

## See Also

### Inspecting what Siri does
- [let response: SiriTranscript.Observation<String>](./response.md)
  The reply Siri concluded the turn with, including an apology or a timeout message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn/intentinvocations)*