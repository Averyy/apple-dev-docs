# intent

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The intent as invoked, carrying the arguments Siri bound to it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let intent: AnyAppIntent
```

## See Also

### Inspecting an invocation
- [let arguments: [String : String]](./arguments.md)
  The arguments Siri passed, as report text.
- [let result: SiriTranscript.Observation<any IntentValueExpressing>?](./result.md)
  The value the invocation returned, an app entity or a scalar or enum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/intent)*