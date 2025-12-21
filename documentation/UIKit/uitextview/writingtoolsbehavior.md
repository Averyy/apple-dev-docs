# writingToolsBehavior

**Framework**: UIKit  
**Kind**: property

The level of Writing Tools support to use in the text view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var writingToolsBehavior: UIWritingToolsBehavior { get set }
```

#### Discussion

The system chooses an initial value based on the device’s capabilities. The value in this property is never the default option, and is instead one of the specific options such as [`UIWritingToolsBehavior.none`](uiwritingtoolsbehavior/none.md), [`UIWritingToolsBehavior.limited`](uiwritingtoolsbehavior/limited.md), or [`UIWritingToolsBehavior.complete`](uiwritingtoolsbehavior/complete.md). Change the initial value to customize your text view’s Writing Tools support.

## See Also

- [var allowedWritingToolsResultOptions: UIWritingToolsResultOptions](uitextview/allowedwritingtoolsresultoptions.md)
  The type of content Writing Tools generates for your text view.
- [var isWritingToolsActive: Bool](uitextview/iswritingtoolsactive.md)
  A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [var writingToolsCoordinator: UIWritingToolsCoordinator](uitextview/writingtoolscoordinator.md)
  The object that coordinates interactions between Writing Tools and the text view.
- [var subclassForWritingToolsCoordinator: AnyClass](uitextview/subclassforwritingtoolscoordinator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/writingtoolsbehavior)*