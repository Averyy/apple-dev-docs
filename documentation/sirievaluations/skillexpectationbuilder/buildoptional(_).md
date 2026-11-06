# buildOptional(_:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a component from a conditional statement with no alternative branch.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func buildOptional(_ component: [SkillDefinition]?) -> [SkillDefinition]
```

## See Also

### Building results
- [static func buildArray([[SkillDefinition]]) -> [SkillDefinition]](./buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([SkillDefinition]...) -> [SkillDefinition]](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [SkillDefinition]) -> [SkillDefinition]](./buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: [SkillDefinition]) -> [SkillDefinition]](./buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(SkillDefinition) -> [SkillDefinition]](./buildexpression%28_%29.md)
  Creates a component from a skill definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/skillexpectationbuilder/buildoptional(_:))*