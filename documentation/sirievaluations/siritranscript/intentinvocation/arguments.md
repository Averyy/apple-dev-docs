# arguments

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The arguments Siri passed, as report text.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let arguments: [String : String]
```

## Discussion

For example, `nights: "4"`. This is for reading only; grading reads `intent`, never this value.

## See Also

### Inspecting an invocation
- [let intent: AnyAppIntent](./intent.md)
  The intent as invoked, carrying the arguments Siri bound to it.
- [let result: SiriTranscript.Observation<any IntentValueExpressing>?](./result.md)
  The value the invocation returned, an app entity or a scalar or enum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/arguments)*