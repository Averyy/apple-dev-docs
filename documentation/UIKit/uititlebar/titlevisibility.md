# titleVisibility

**Framework**: UIKit  
**Kind**: property

A value that indicates the visibility of the title.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
var titleVisibility: UITitlebarTitleVisibility { get set }
```

## Mentions

- [Removing the title bar in your Mac app built with Mac Catalyst](removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst.md)

#### Discussion

Setting the title visibility to [`UITitlebarTitleVisibility.hidden`](uititlebartitlevisibility/hidden.md) hides only the title displayed in the title bar, not the title bar itself. To remove the title bar from the window, set [`titleVisibility`](uititlebar/titlevisibility.md) to [`UITitlebarTitleVisibility.hidden`](uititlebartitlevisibility/hidden.md) and [`toolbar`](uititlebar/toolbar.md) to `nil`.

This property defaults to [`UITitlebarTitleVisibility.visible`](uititlebartitlevisibility/visible.md).

## See Also

- [var separatorStyle: UITitlebarSeparatorStyle](uititlebar/separatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum UITitlebarSeparatorStyle](uititlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [enum UITitlebarTitleVisibility](uititlebartitlevisibility.md)
  States that determine visibility of the title in the title bar.
- [var representedURL: URL?](uititlebar/representedurl.md)
  A URL of the file or resource represented in the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebar/titlevisibility)*