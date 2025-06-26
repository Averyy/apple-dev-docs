# menuItem

**Framework**: WebKit  
**Kind**: property

A menu item representation of the web extension command for use in menus.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@NSCopying
@MainActor var menuItem: NSMenuItem { get }
```

#### Discussion

Provides a representation of the web extension command as a menu item to display in the app.

Selecting the menu item will perform the command, offering a convenient and visual way for users to execute this web extension command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/command/menuitem)*