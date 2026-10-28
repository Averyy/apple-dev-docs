# autoHidesToolbarInFullScreen

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the toolbar automatically hides in full-screen windows.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
var autoHidesToolbarInFullScreen: Bool { get set }
```

```objc
@property (nonatomic) BOOL autoHidesToolbarInFullScreen;
```

## Discussion

Set this property to [`true`](../../Swift/true.md) to automatically hide the toolbar when the window enters full-screen mode. While hidden, the user can view the toolbar and menu bar by moving the pointer to the top of the screen. Moving the pointer away from the top of the screen hides the toolbar and menu bar.

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the toolbar
- [var toolbar: NSToolbar?](./toolbar.md)
  The toolbar displayed beneath or integrated with the title bar.
- [var toolbarStyle: UITitlebarToolbarStyle](./toolbarstyle.md)
  The style of the toolbar determining its appearance and location related to the title bar.
- [enum UITitlebarToolbarStyle](../uititlebartoolbarstyle.md)
  Styles that determine the toolbar’s appearance and location related to the title bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebar/autohidestoolbarinfullscreen)*