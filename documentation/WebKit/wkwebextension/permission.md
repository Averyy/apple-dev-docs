# WKWebExtension.Permission

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Constants for specifying permission in a [`WKWebExtensionContext`](../wkwebextensioncontext.md).

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct Permission
```

```c
typedef NSString * WKWebExtensionPermission;
```

## Topics

### Constants
- [static let activeTab: WKWebExtension.Permission](./permission/activetab.md)
  A request indicating that when a person interacts with the extension, the system grants extra permissions for the active tab only.
- [static let alarms: WKWebExtension.Permission](./permission/alarms.md)
  A request for access to the `browser.alarms` APIs.
- [static let clipboardWrite: WKWebExtension.Permission](./permission/clipboardwrite.md)
  A request for access to write to the clipboard.
- [static let contextMenus: WKWebExtension.Permission](./permission/contextmenus.md)
  A request for access to the `browser.contextMenus` APIs.
- [static let cookies: WKWebExtension.Permission](./permission/cookies.md)
  A request for access to the `browser.cookies` APIs.
- [static let declarativeNetRequest: WKWebExtension.Permission](./permission/declarativenetrequest.md)
  A request for access to the `browser.declarativeNetRequest` APIs.
- [static let declarativeNetRequestFeedback: WKWebExtension.Permission](./permission/declarativenetrequestfeedback.md)
  A request for access to the `browser.declarativeNetRequest` APIs with extra information on matched rules.
- [static let declarativeNetRequestWithHostAccess: WKWebExtension.Permission](./permission/declarativenetrequestwithhostaccess.md)
  A request for access to the `browser.declarativeNetRequest` APIs with the ability to modify or redirect requests.
- [static let menus: WKWebExtension.Permission](./permission/menus.md)
  A request for access to the `browser.menus` APIs.
- [static let nativeMessaging: WKWebExtension.Permission](./permission/nativemessaging.md)
  A request for access to send messages to the app extension bundle.
- [static let scripting: WKWebExtension.Permission](./permission/scripting.md)
  A request for access to the `browser.scripting` APIs.
- [static let storage: WKWebExtension.Permission](./permission/storage.md)
  A request for access to the `browser.storage` APIs.
- [static let tabs: WKWebExtension.Permission](./permission/tabs.md)
  A request for access to extra information on the `browser.tabs` APIs.
- [static let unlimitedStorage: WKWebExtension.Permission](./permission/unlimitedstorage.md)
  A request for access to an unlimited quota on the `browser.storage.local` APIs.
- [static let webNavigation: WKWebExtension.Permission](./permission/webnavigation.md)
  A request for access to the `browser.webNavigation` APIs.
- [static let webRequest: WKWebExtension.Permission](./permission/webrequest.md)
  A request for access to the `browser.webRequest` APIs.
### Initializers
- [init(String)](./permission/init%28_%29.md)
- [init(rawValue: String)](./permission/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Structures
- [WKWebExtension.DataType](./datatype.md)
  Constants for specifying data types for a [`WKWebExtension.DataRecord`](./datarecord.md).
- [WKWebExtension.Error](./error.md)
  Constants that indicate errors in the [`WKWebExtension`](../wkwebextension.md) domain.
- [WKWebExtension.TabChangedProperties](./tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/permission)*