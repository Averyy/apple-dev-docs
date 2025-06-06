# PlaygroundPage.AssessmentStatus.fail(hints:solution:)

**Framework**: Playground Support  
**Kind**: enumelt

An assessment that communicates that a learner hasn't successfully completed a task.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case fail(hints: [String], solution: String?)
```

#### Discussion

If no solution is provided, there must be at least one string in the `hints` array.

The strings for the solution and for hints can contain markup. For more information on markup, see [`Markup Formatting Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497). The example below sets one hint for the page. The markup in the hint string displays the word “for” in code voice.

```swift
PlaygroundPage.current.assessmentStatus = .fail(hints: ["Try using a `for` loop"], solution: nil)
```

## Parameters

- `hints`: A list of hints that might help a learner pass the assessment.
- `solution`: An explicit solution to the assessment that a learner can use to get unstuck.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/assessmentstatus/fail_hints_solution)*