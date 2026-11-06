# SiriTranscript.Observation

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

A value from the run, with the time the framework built its transcript.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct Observation<Value> where Value : Sendable
```

## Overview

Every observation in a transcript carries the same timestamp, so timestamps say nothing about order, timing, or which value Siri used.

## Topics

### Inspecting an observation
- [let value: Value](./observation/value.md)
  The value the framework recorded.
- [let timestamp: Date](./observation/timestamp.md)
  The time the framework built the transcript that holds this observation.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading transcript contents
- [SiriTranscript.Turn](./turn.md)
  Everything observed during one user turn.
- [SiriTranscript.IntentInvocation](./intentinvocation.md)
  A record of one intent call, including its arguments and result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/observation)*