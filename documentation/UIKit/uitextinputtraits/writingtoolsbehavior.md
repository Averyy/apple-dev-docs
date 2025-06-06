# writingToolsBehavior

**Framework**: UIKit  
**Kind**: property

The writing tools experience to support in the current view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional var writingToolsBehavior: UIWritingToolsBehavior { get set }
```

## Mentions

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md)

#### Discussion

Use this property to specify the type of experience to display when someone engages writing tools for a text input view. The system does its best to provide the requested UI, but might offer a more limited experience if required capabilities aren’t available. The default value of this property is [`UIWritingToolsBehavior.default`](uiwritingtoolsbehavior/default.md), which lets the system choose the most appropriate experience for the current device.

Set the value of this property to [`UIWritingToolsBehavior.none`](uiwritingtoolsbehavior/none.md) if you want to prevent someone from using the writing tools with your view.

## See Also

- [enum UIWritingToolsBehavior](uiwritingtoolsbehavior.md)
  Constants that specify the writing tools experience for the underlying view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/writingtoolsbehavior)*