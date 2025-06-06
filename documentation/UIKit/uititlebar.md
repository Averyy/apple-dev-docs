# UITitlebar

**Framework**: UIKit  
**Kind**: class

An object that you use to configure the title bar of a window in a Mac app built with Mac Catalyst.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
class UITitlebar
```

#### Overview

Each [`UIWindowScene`](uiwindowscene.md) has a [`UITitlebar`](uititlebar.md) object available in Mac apps built with Mac Catalyst. You use this object to configure the title bar and its toolbar.

To show or hide a title in the title bar, set the [`titleVisibility`](uititlebar/titlevisibility.md) property to [`UITitlebarTitleVisibility.visible`](uititlebartitlevisibility/visible.md) or [`UITitlebarTitleVisibility.hidden`](uititlebartitlevisibility/hidden.md). If you set the visibility to hidden and the title bar’s [`toolbar`](uititlebar/toolbar.md) property is `nil`, the window displays only the window control buttons (Close, Minimize, and Zoom).

To add a toolbar to a window, create an [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) object and assign it to the title bar’s [`toolbar`](uititlebar/toolbar.md) property. To automatically hide the toolbar when the window enters full-screen mode, set the [`autoHidesToolbarInFullScreen`](uititlebar/autohidestoolbarinfullscreen.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    
    guard let windowScene = (scene as? UIWindowScene) else { return }
    
    #if targetEnvironment(macCatalyst)
    if  let titlebar = windowScene.titlebar {
        let identifier = NSToolbar.Identifier("com.example.apple-samplecode.toolbar")
        titlebar.toolbar = NSToolbar(identifier: identifier)
        titlebar.toolbar?.delegate = self
        titlebar.autoHidesToolbarInFullScreen = true
    }
    #endif
}
```

## Topics

### Configuring the title bar
- [var separatorStyle: UITitlebarSeparatorStyle](uititlebar/separatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum UITitlebarSeparatorStyle](uititlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var titleVisibility: UITitlebarTitleVisibility](uititlebar/titlevisibility.md)
  A value that indicates the visibility of the title.
- [enum UITitlebarTitleVisibility](uititlebartitlevisibility.md)
  States that determine visibility of the title in the title bar.
- [var representedURL: URL?](uititlebar/representedurl.md)
  A URL of the file or resource represented in the window.
### Configuring the toolbar
- [var toolbar: NSToolbar?](uititlebar/toolbar.md)
  The toolbar displayed beneath or integrated with the title bar.
- [var toolbarStyle: UITitlebarToolbarStyle](uititlebar/toolbarstyle.md)
  The style of the toolbar determining its appearance and location related to the title bar.
- [enum UITitlebarToolbarStyle](uititlebartoolbarstyle.md)
  Styles that determine the toolbar’s appearance and location related to the title bar.
- [var autoHidesToolbarInFullScreen: Bool](uititlebar/autohidestoolbarinfullscreen.md)
  A Boolean value that determines whether the toolbar automatically hides in full-screen windows.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var titlebar: UITitlebar?](uiwindowscene/titlebar.md)
  The title bar displayed in a window of a Mac app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebar)*