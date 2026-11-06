# loadedSkills

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The App Skills Siri loaded into its planning this turn.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let loadedSkills: [SiriTranscript.Observation<SkillDefinition>]
```

## Discussion

Identity-based, by app and name: a skill carries no properties to observe, only whether Siri loaded it.

## See Also

### Accessing the turn’s context
- [let foundEntities: [SiriTranscript.Observation<AnyAppEntity>]](./foundentities.md)
  The entities Siri surfaced by search or resolution, with the properties Siri read for them before its next intent ran.
- [let onScreenEntities: [SiriTranscript.Observation<AnyAppEntity>]](./onscreenentities.md)
  The entities Siri captured as onscreen context, with the properties Siri read for them before its next intent ran.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siritranscript/turn/loadedskills)*