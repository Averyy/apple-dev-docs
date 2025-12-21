# writingToolsCoordinator

**Framework**: UIKit  
**Kind**: property

The object that coordinates interactions between Writing Tools and the text view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var writingToolsCoordinator: UIWritingToolsCoordinator { get }
```

#### Discussion

When you get the value of this property, the system creates a Writing Tools coordinator object if one doesn’t already exist for this view.

## See Also

- [var writingToolsBehavior: UIWritingToolsBehavior](uitextview/writingtoolsbehavior.md)
  The level of Writing Tools support to use in the text view.
- [var allowedWritingToolsResultOptions: UIWritingToolsResultOptions](uitextview/allowedwritingtoolsresultoptions.md)
  The type of content Writing Tools generates for your text view.
- [var isWritingToolsActive: Bool](uitextview/iswritingtoolsactive.md)
  A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [var subclassForWritingToolsCoordinator: AnyClass](uitextview/subclassforwritingtoolscoordinator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/writingtoolscoordinator)*