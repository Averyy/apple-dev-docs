# allowedWritingToolsResultOptions

**Framework**: UIKit  
**Kind**: property

The type of content Writing Tools generates for your text view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var allowedWritingToolsResultOptions: UIWritingToolsResultOptions { get set }
```

#### Discussion

Text views support most types of generated content. However, if you set this property to a value that includes the [`table`](uiwritingtoolsresultoptions/table.md) option, UIKit raises [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException).

## See Also

- [var writingToolsBehavior: UIWritingToolsBehavior](uitextview/writingtoolsbehavior.md)
  The level of Writing Tools support to use in the text view.
- [var isWritingToolsActive: Bool](uitextview/iswritingtoolsactive.md)
  A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [var writingToolsCoordinator: UIWritingToolsCoordinator](uitextview/writingtoolscoordinator.md)
  The object that coordinates interactions between Writing Tools and the text view.
- [var subclassForWritingToolsCoordinator: AnyClass](uitextview/subclassforwritingtoolscoordinator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/allowedwritingtoolsresultoptions)*