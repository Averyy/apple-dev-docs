# SiriTranscript.Turn

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

Everything observed during one user turn.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct Turn
```

## Topics

### Inspecting what Siri does
- [let intentInvocations: [SiriTranscript.Observation<SiriTranscript.IntentInvocation>]](./turn/intentinvocations.md)
  The intents Siri invoked during the turn, with the arguments it bound.
- [let response: SiriTranscript.Observation<String>](./turn/response.md)
  The reply Siri concluded the turn with, including an apology or a timeout message.
### Identifying a turn
- [let id: UUID](./turn/id.md)
  The identifier of the user turn that produced this turn.
### Accessing the turn’s context
- [let foundEntities: [SiriTranscript.Observation<AnyAppEntity>]](./turn/foundentities.md)
  The entities Siri surfaced by search or resolution, with the properties Siri read for them before its next intent ran.
- [let onScreenEntities: [SiriTranscript.Observation<AnyAppEntity>]](./turn/onscreenentities.md)
  The entities Siri captured as onscreen context, with the properties Siri read for them before its next intent ran.
- [let loadedSkills: [SiriTranscript.Observation<SkillDefinition>]](./turn/loadedskills.md)
  The App Skills Siri loaded into its planning this turn.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading transcript contents
- [SiriTranscript.IntentInvocation](./intentinvocation.md)
  A record of one intent call, including its arguments and result.
- [SiriTranscript.Observation](./observation.md)
  A value from the run, with the time the framework built its transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn)*