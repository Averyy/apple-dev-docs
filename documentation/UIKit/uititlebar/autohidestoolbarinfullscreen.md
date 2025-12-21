# autoHidesToolbarInFullScreen

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the toolbar automatically hides in full-screen windows.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
var autoHidesToolbarInFullScreen: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to automatically hide the toolbar when the window enters full-screen mode. While hidden, the user can view the toolbar and menu bar by moving the pointer to the top of the screen. Moving the pointer away from the top of the screen hides the toolbar and menu bar.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var toolbar: NSToolbar?](uititlebar/toolbar.md)
  The toolbar displayed beneath or integrated with the title bar.
- [var toolbarStyle: UITitlebarToolbarStyle](uititlebar/toolbarstyle.md)
  The style of the toolbar determining its appearance and location related to the title bar.
- [enum UITitlebarToolbarStyle](uititlebartoolbarstyle.md)
  Styles that determine the toolbar’s appearance and location related to the title bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebar/autohidestoolbarinfullscreen)*