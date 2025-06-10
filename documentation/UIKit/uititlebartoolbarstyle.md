# UITitlebarToolbarStyle

**Framework**: UIKit  
**Kind**: enum

Styles that determine the toolbar’s appearance and location related to the title bar.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```swift
enum UITitlebarToolbarStyle
```

## Topics

### Styles
- [UITitlebarToolbarStyle.automatic](uititlebartoolbarstyle/automatic.md)
  A style indicating that the system determines the toolbar’s appearance and location.
- [UITitlebarToolbarStyle.expanded](uititlebartoolbarstyle/expanded.md)
  A style indicating that the toolbar appears below the window title.
- [UITitlebarToolbarStyle.preference](uititlebartoolbarstyle/preference.md)
  A style indicating that the toolbar appears below the window title with toolbar items centered in the toolbar.
- [UITitlebarToolbarStyle.unified](uititlebartoolbarstyle/unified.md)
  A style indicating that the toolbar appears inline with the window title.
- [UITitlebarToolbarStyle.unifiedCompact](uititlebartoolbarstyle/unifiedcompact.md)
  A style indicating that the toolbar appears inline with the window title and with reduced margins to allow more focus on the window’s contents.
### Initializers
- [init?(rawValue: Int)](uititlebartoolbarstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var toolbar: NSToolbar?](uititlebar/toolbar.md)
  The toolbar displayed beneath or integrated with the title bar.
- [var toolbarStyle: UITitlebarToolbarStyle](uititlebar/toolbarstyle.md)
  The style of the toolbar determining its appearance and location related to the title bar.
- [var autoHidesToolbarInFullScreen: Bool](uititlebar/autohidestoolbarinfullscreen.md)
  A Boolean value that determines whether the toolbar automatically hides in full-screen windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebartoolbarstyle)*