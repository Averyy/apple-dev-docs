# outcome

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

How the call ended.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let outcome: SiriTranscript.IntentInvocation.Outcome
```

## Discussion

Siri plans a call before it runs it, and a planned call can stop short. Only a call that ran satisfies `Calls`. `Calls(.disallowed)` fails on a call that ran, on one Siri put to the person to confirm (by then Siri has chosen the action and its arguments, and only the person’s answer stands between the request and the action), and on one with no outcome recorded.

## See Also

### Determining the outcome
- [SiriTranscript.IntentInvocation.Outcome](./outcome-swift.enum.md)
  How a call Siri planned ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/intentinvocation/outcome-swift.property)*