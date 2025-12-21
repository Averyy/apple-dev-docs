# menuItems

**Framework**: WebKit  
**Kind**: property

The menu items provided by the extension for this action.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var menuItems: [NSMenuItem] { get }
```

#### Discussion

Provides menu items supplied by the extension, allowing the user to perform extension-defined actions.

The app is responsible for displaying these menu items, typically in a context menu or a long-press menu on the action in action sheets or toolbars.

> **Note**: The properties of the menu items, including the items themselves, can change dynamically. Therefore, the app should fetch the menu items on demand immediately before showing them, to ensure that the most current and relevant items are presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/menuitems)*