# isWritingToolsActive

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var isWritingToolsActive: Bool { get }
```

#### Discussion

Use this property to determine when someone is using the writing tools to rewrite text in the current text view. When writing tools are active, the system can change significant portions of the text view’s content. You might use this property to prevent your app from performing actions that interfere with those changes. For example, you might stop synchronizing text to iCloud while the UI is active.

To receive notifications when writing tools interactions start and stop, implement the  [`textViewWritingToolsWillBegin(_:)`](uitextviewdelegate/textviewwritingtoolswillbegin(_:).md) and [`textViewWritingToolsDidEnd(_:)`](uitextviewdelegate/textviewwritingtoolsdidend(_:).md) delegate methods.

## See Also

- [var writingToolsBehavior: UIWritingToolsBehavior](uitextview/writingtoolsbehavior.md)
  The level of Writing Tools support to use in the text view.
- [var allowedWritingToolsResultOptions: UIWritingToolsResultOptions](uitextview/allowedwritingtoolsresultoptions.md)
  The type of content Writing Tools generates for your text view.
- [var writingToolsCoordinator: UIWritingToolsCoordinator](uitextview/writingtoolscoordinator.md)
  The object that coordinates interactions between Writing Tools and the text view.
- [var subclassForWritingToolsCoordinator: AnyClass](uitextview/subclassforwritingtoolscoordinator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/iswritingtoolsactive)*