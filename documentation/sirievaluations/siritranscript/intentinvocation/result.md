# result

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The value the invocation returned, an app entity or a scalar or enum value.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let result: SiriTranscript.Observation<any IntentValueExpressing>?
```

## Discussion

An entity carries the properties the call returned with it; one returned as a reference, only the properties the scenario’s `.result(…)` checks name, as its app returned them after the call, one it returned the entity without having no value unless it’s a `@DeferredProperty`. `SiriExpectationEvaluator` fails a check on any other of its properties, one that wasn’t read (the read failed or timed out), and one holding a list of more than 100 items, and a predicate (`.matches(_:)`) over such a reference, which can read a property that wasn’t read. It fails a check on the result’s `id`, which isn’t a property; use `expectIdentifier(_:)`. When Siri starts another intent of your app before that read finishes, it carries none, so its checks fail, the report saying they’re unable to be graded reliably. `nil` means nothing was recorded: the call returned nothing, or the value could not be decoded (see `resultUndecoded`). A collection result is represented by its first element.

## See Also

### Inspecting an invocation
- [let intent: AnyAppIntent](./intent.md)
  The intent as invoked, carrying the arguments Siri bound to it.
- [let arguments: [String : String]](./arguments.md)
  The arguments Siri passed, as report text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/result)*