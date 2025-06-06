# kNoEndingProsody

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var kNoEndingProsody: Int32 { get }
```

#### Discussion

Disables prosody at end of sentences. The `kNoEndingProsody` flagbit is used to control whether or not the speech synthesizer automaticallyapplies ending prosody, the speech tone and cadence that normallyoccur at the end of a statement. Under normal circumstances (forexample, when the flag bit is not set), ending prosody is appliedto the speech when the end of the `textBuf` datais reached. This default behavior can be disabled by setting the `kNoEndingProsody` flagbit.

Some synthesizers do not speak until the `kNoEndingProsody` flagbit is reset, or they encounter a period in the text, or `textBuf` isfull.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/knoendingprosody)*