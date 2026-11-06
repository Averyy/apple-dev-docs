# SiriTranscript.IntentInvocation

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

A record of one intent call, including its arguments and result.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct IntentInvocation
```

## Topics

### Inspecting an invocation
- [let intent: AnyAppIntent](./intentinvocation/intent.md)
  The intent as invoked, carrying the arguments Siri bound to it.
- [let arguments: [String : String]](./intentinvocation/arguments.md)
  The arguments Siri passed, as report text.
- [let result: SiriTranscript.Observation<any IntentValueExpressing>?](./intentinvocation/result.md)
  The value the invocation returned, an app entity or a scalar or enum value.
### Determining the outcome
- [let outcome: SiriTranscript.IntentInvocation.Outcome](./intentinvocation/outcome-swift.property.md)
  How the call ended.
- [SiriTranscript.IntentInvocation.Outcome](./intentinvocation/outcome-swift.enum.md)
  How a call Siri planned ended.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading transcript contents
- [SiriTranscript.Turn](./turn.md)
  Everything observed during one user turn.
- [SiriTranscript.Observation](./observation.md)
  A value from the run, with the time the framework built its transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation)*