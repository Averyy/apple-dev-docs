# value

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The run as the report shows it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var value: SiriScenarioSubject.ScenarioReport { get }
```

## Discussion

The sections are Diagnostics, Scenario (if it has any expectations of its own), then each turn: what the person said, each expectation set beside what Siri did, and Siri’s response. It’s text for display, not a format to parse.

A turn that never ran still appears, saying so. Dropping it would shift later turns into earlier positions and make the report quietly wrong.

## See Also

### Inspecting the subject
- [let siriTranscript: SiriTranscript](./siritranscript.md)
  Every observation captured during the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenariosubject/value)*