# foundEntities

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The entities Siri surfaced by search or resolution, with the properties Siri read for them before its next intent ran.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let foundEntities: [SiriTranscript.Observation<AnyAppEntity>]
```

## See Also

### Accessing the turn’s context
- [let onScreenEntities: [SiriTranscript.Observation<AnyAppEntity>]](./onscreenentities.md)
  The entities Siri captured as onscreen context, with the properties Siri read for them before its next intent ran.
- [let loadedSkills: [SiriTranscript.Observation<SkillDefinition>]](./loadedskills.md)
  The App Skills Siri loaded into its planning this turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn/foundentities)*