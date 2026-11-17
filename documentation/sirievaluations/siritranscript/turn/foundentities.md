# foundEntities

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The entities Siri surfaced by search or resolution.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let foundEntities: [SiriTranscript.Observation<AnyAppEntity>]
```

## Discussion

Each carries the properties Siri’s search returned with it; a reference, the properties the scenario checks, as its app indexed them in Spotlight or, where the index couldn’t give them (see `Finds`), as the app returned them, read when Siri found it. A property that wasn’t read for a reference reads as `nil` here: only `SiriExpectationEvaluator` tells it apart from one with no value, and fails a check on it.

## See Also

### Accessing the turn’s context
- [let onScreenEntities: [SiriTranscript.Observation<AnyAppEntity>]](./onscreenentities.md)
  The entities Siri captured as onscreen context, as Siri recorded them.
- [let loadedSkills: [SiriTranscript.Observation<SkillDefinition>]](./loadedskills.md)
  The App Skills Siri loaded into its planning this turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn/foundentities)*