# menuItem

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A menu item representation of the web extension command for use in menus.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
@NSCopying
var menuItem: UIMenuElement { get }
```

*macOS*

```swift
@NSCopying
var menuItem: NSMenuItem { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, copy, readonly) UIMenuElement * menuItem;
```

*macOS*

```objc
@property (nonatomic, copy, readonly) NSMenuItem * menuItem;
```

#### Discussion

Provides a representation of the web extension command as a menu item to display in the app.

Selecting the menu item will perform the command, offering a convenient and visual way for users to execute this web extension command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/command/menuitem)*