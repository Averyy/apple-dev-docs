# SiriTranscript

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

The immutable record of one scenario’s execution.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct SiriTranscript
```

## Overview

A transcript records what Siri does while running one scenario. For each turn, it holds:

- the intents Siri calls, with their arguments
- how each call ends
- the entities Siri finds
- the entities onscreen
- the skills Siri loads
- the reply Siri gives

A [`SiriExpectationEvaluator`](./siriexpectationevaluator.md) reads the transcript to compute metrics. When you write an evaluator of your own, read the transcript through the [`siriTranscript`](./siriscenariosubject/siritranscript.md) property of the evaluation subject. The transcript holds calls, entities, and skills only for the apps your scenario’s expectations name, and never for Apple’s apps. It also doesn’t mark a turn that the run cuts short, so don’t treat a call or skill that’s missing from it as proof that Siri didn’t use it. Siri’s reply, the arguments of a recorded call, and the values nested in a recorded entity aren’t filtered by app, so they can include another app’s data.

Look up a turn with [`turn(for:)`](./siritranscript/turn%28for%29.md) using the identifier of the [`UserTurn`](./userturn.md) that produces it, not its position. Identifier lookup keeps a run that stops early from pairing a recorded turn with the wrong turn from the scenario.

The following shows a function that counts the intents Siri runs during a turn, or returns `nil` for a turn the run never reaches:

```swift
func ranIntentCount(for turn: UserTurn, in subject: SiriScenarioSubject) -> Int? {
    // Look up the recorded turn by the identifier. A turn the run
    // never reaches has no record.
    guard let recorded = subject.siriTranscript.turn(for: turn.id) else {
        return nil
    }

    // Count the calls that run, not the ones that stop to ask a
    // question or fail.
    return recorded.intentInvocations
        .filter { $0.value.outcome.ran }
        .count
}
```

## Topics

### Inspecting a transcript
- [let turns: [SiriTranscript.Turn]](./siritranscript/turns.md)
  The turns the run reached, in conversation order.
- [func turn(for: UUID) -> SiriTranscript.Turn?](./siritranscript/turn%28for%29.md)
  Returns the turn produced by the scenario turn with this identity, if it ran.
### Reading transcript contents
- [SiriTranscript.Turn](./siritranscript/turn.md)
  Everything observed during one user turn.
- [SiriTranscript.IntentInvocation](./siritranscript/intentinvocation.md)
  A record of one intent call, including its arguments and result.
- [SiriTranscript.Observation](./siritranscript/observation.md)
  A value from the run, with the time the framework built its transcript.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Results
- [struct SiriScenarioSubject](./siriscenariosubject.md)
  A record of one scenario’s run through Siri, as the Evaluations framework sees it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript)*