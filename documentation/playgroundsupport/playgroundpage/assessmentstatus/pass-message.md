# PlaygroundPage.AssessmentStatus.pass(message:)

**Framework**: Playground Support  
**Kind**: enumelt

An assessment that communicates that a learner has successfully completed a task.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case pass(message: String?)
```

#### Discussion

The `message` associated value can contain markup. For more information on markup, see [`Markup Formatting Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497). The example below shows a popover with the message “ job!”

```swift
PlaygroundPage.current.assessmentStatus = .pass(message: "**Great** job!")
```

## Parameters

- `message`: A message you use to affirm a learner's succes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/assessmentstatus/pass_message)*