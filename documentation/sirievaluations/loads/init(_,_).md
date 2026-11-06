# init(_:_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates an expectation that the skills in the block load, graded according to the enforcement.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(_ enforcement: Loads.Enforcement, @SkillExpectationBuilder _ content: () -> [SkillDefinition])
```

## Discussion

Written `Loads(.required) { organizeEventSkill }` or `Loads(.preferred) { organizeEventSkill }`.

## See Also

### Creating a load expectation
- [enum SkillExpectationBuilder](../skillexpectationbuilder.md)
  A result builder that collects the skills in a loads expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/loads/init(_:_:))*