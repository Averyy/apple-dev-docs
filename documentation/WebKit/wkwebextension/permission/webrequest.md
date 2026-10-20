# webRequest

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

A request for access to the `browser.webRequest` APIs.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
static let webRequest: WKWebExtension.Permission
```

```c
extern WKWebExtensionPermission const WKWebExtensionPermissionWebRequest;
```

## See Also

### Constants
- [static let activeTab: WKWebExtension.Permission](./activetab.md)
  A request indicating that when a person interacts with the extension, the system grants extra permissions for the active tab only.
- [static let alarms: WKWebExtension.Permission](./alarms.md)
  A request for access to the `browser.alarms` APIs.
- [static let clipboardWrite: WKWebExtension.Permission](./clipboardwrite.md)
  A request for access to write to the clipboard.
- [static let contextMenus: WKWebExtension.Permission](./contextmenus.md)
  A request for access to the `browser.contextMenus` APIs.
- [static let cookies: WKWebExtension.Permission](./cookies.md)
  A request for access to the `browser.cookies` APIs.
- [static let declarativeNetRequest: WKWebExtension.Permission](./declarativenetrequest.md)
  A request for access to the `browser.declarativeNetRequest` APIs.
- [static let declarativeNetRequestFeedback: WKWebExtension.Permission](./declarativenetrequestfeedback.md)
  A request for access to the `browser.declarativeNetRequest` APIs with extra information on matched rules.
- [static let declarativeNetRequestWithHostAccess: WKWebExtension.Permission](./declarativenetrequestwithhostaccess.md)
  A request for access to the `browser.declarativeNetRequest` APIs with the ability to modify or redirect requests.
- [static let menus: WKWebExtension.Permission](./menus.md)
  A request for access to the `browser.menus` APIs.
- [static let nativeMessaging: WKWebExtension.Permission](./nativemessaging.md)
  A request for access to send messages to the app extension bundle.
- [static let scripting: WKWebExtension.Permission](./scripting.md)
  A request for access to the `browser.scripting` APIs.
- [static let storage: WKWebExtension.Permission](./storage.md)
  A request for access to the `browser.storage` APIs.
- [static let tabs: WKWebExtension.Permission](./tabs.md)
  A request for access to extra information on the `browser.tabs` APIs.
- [static let unlimitedStorage: WKWebExtension.Permission](./unlimitedstorage.md)
  A request for access to an unlimited quota on the `browser.storage.local` APIs.
- [static let webNavigation: WKWebExtension.Permission](./webnavigation.md)
  A request for access to the `browser.webNavigation` APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/permission/webrequest)*