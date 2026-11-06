# SkillExpectationBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the skills in a loads expectation.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum SkillExpectationBuilder
```

## Overview

It accepts the App Skills inside a [`Loads`](./loads.md) block by identity: a bare `SkillDefinition` (`definitions.skills["organize-event"]`). A skill has no properties to constrain, only whether Siri loaded it, so there is no `.expect` form here.

## Topics

### Building results
- [static func buildArray([[SkillDefinition]]) -> [SkillDefinition]](./skillexpectationbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([SkillDefinition]...) -> [SkillDefinition]](./skillexpectationbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [SkillDefinition]) -> [SkillDefinition]](./skillexpectationbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: [SkillDefinition]) -> [SkillDefinition]](./skillexpectationbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(SkillDefinition) -> [SkillDefinition]](./skillexpectationbuilder/buildexpression%28_%29.md)
  Creates a component from a skill definition.
- [static func buildOptional([SkillDefinition]?) -> [SkillDefinition]](./skillexpectationbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.

## See Also

### Creating a load expectation
- [init(Loads.Enforcement, () -> [SkillDefinition])](./loads/init%28_,_%29.md)
  Creates an expectation that the skills in the block load, graded according to the enforcement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/skillexpectationbuilder)*