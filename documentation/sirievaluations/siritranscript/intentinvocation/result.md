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

An entity carries the properties Siri read for it after the call ran, or only what Siri recorded with it if Siri read none. `nil` means nothing was recorded: the call returned nothing, or the value could not be decoded (see `resultUndecoded`). A collection result is represented by its first element.

## See Also

### Inspecting an invocation
- [let intent: AnyAppIntent](./intent.md)
  The intent as invoked, carrying the arguments Siri bound to it.
- [let arguments: [String : String]](./arguments.md)
  The arguments Siri passed, as report text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/result)*