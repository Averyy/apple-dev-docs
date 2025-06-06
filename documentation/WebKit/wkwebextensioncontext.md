# WKWebExtensionContext

**Framework**: Webkit  
**Kind**: class

An object that represents the runtime environment for a web extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class WKWebExtensionContext
```

#### Overview

This class provides methods for managing the extension’s permissions, allowing it to inject content, run background logic, show popovers, and display other web-based UI to the user.

## Topics

### Enumerations
- [WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus.md)
  Constants used to indicate permission status in web extension context.
### Structures
- [WKWebExtensionContext.Error](wkwebextensioncontext/error.md)
  Constants used to indicate errors in the web extension context domain.
- [WKWebExtensionContext.NotificationUserInfoKey](wkwebextensioncontext/notificationuserinfokey.md)
  Constants for specifying web extension context information in notifications.
### Initializers
- [init(for: WKWebExtension)](wkwebextensioncontext/init(for:).md)
  Returns a web extension context initialized with a specified extension.
### Instance Properties
- [var baseURL: URL](wkwebextensioncontext/baseurl.md)
  The base URL the context uses for loading extension resources or injecting content into webpages.
- [var commands: [WKWebExtension.Command]](wkwebextensioncontext/commands.md)
  The commands associated with the extension.
- [var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](wkwebextensioncontext/currentpermissionmatchpatterns.md)
  The currently granted permission match patterns that have not expired.
- [var currentPermissions: Set<WKWebExtension.Permission>](wkwebextensioncontext/currentpermissions.md)
  The currently granted permissions that have not expired.
- [var deniedPermissionMatchPatterns: [WKWebExtension.MatchPattern : Date]](wkwebextensioncontext/deniedpermissionmatchpatterns.md)
  The currently denied permission match patterns and their expiration dates.
- [var deniedPermissions: [WKWebExtension.Permission : Date]](wkwebextensioncontext/deniedpermissions.md)
  The currently denied permissions and their expiration dates.
- [var errors: [any Error]](wkwebextensioncontext/errors.md)
  All errors that occurred in the extension context.
- [var focusedWindow: (any WKWebExtensionWindow)?](wkwebextensioncontext/focusedwindow.md)
  The window that currently has focus for this extension.
- [var grantedPermissionMatchPatterns: [WKWebExtension.MatchPattern : Date]](wkwebextensioncontext/grantedpermissionmatchpatterns.md)
  The currently granted permission match patterns and their expiration dates.
- [var grantedPermissions: [WKWebExtension.Permission : Date]](wkwebextensioncontext/grantedpermissions.md)
  The currently granted permissions and their expiration dates.
- [var hasAccessToAllHosts: Bool](wkwebextensioncontext/hasaccesstoallhosts.md)
  A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern or any `*` host patterns.
- [var hasAccessToAllURLs: Bool](wkwebextensioncontext/hasaccesstoallurls.md)
  A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern.
- [var hasAccessToPrivateData: Bool](wkwebextensioncontext/hasaccesstoprivatedata.md)
  A Boolean value indicating if the extension has access to private data.
- [var hasContentModificationRules: Bool](wkwebextensioncontext/hascontentmodificationrules.md)
  A boolean value indicating whether the extension includes rules used for content modification or blocking.
- [var hasInjectedContent: Bool](wkwebextensioncontext/hasinjectedcontent.md)
  A Boolean value indicating whether the extension has script or stylesheet content that can be injected into webpages.
- [var hasRequestedOptionalAccessToAllHosts: Bool](wkwebextensioncontext/hasrequestedoptionalaccesstoallhosts.md)
  A Boolean value indicating if the extension has requested optional access to all hosts.
- [var inspectionName: String?](wkwebextensioncontext/inspectionname.md)
  The name shown when inspecting the background web view.
- [var isInspectable: Bool](wkwebextensioncontext/isinspectable.md)
  Determines whether Web Inspector can inspect the [`WKWebView`](wkwebview.md) instances for this context.
- [var isLoaded: Bool](wkwebextensioncontext/isloaded.md)
  A Boolean value indicating if this context is loaded in an extension controller.
- [var openTabs: Set<AnyHashable>](wkwebextensioncontext/opentabs.md)
  A set of open tabs in all open windows that are exposed to this extension.
- [var openWindows: [any WKWebExtensionWindow]](wkwebextensioncontext/openwindows.md)
  The open windows that are exposed to this extension.
- [var optionsPageURL: URL?](wkwebextensioncontext/optionspageurl.md)
  The URL of the extension’s options page, if the extension has one.
- [var overrideNewTabPageURL: URL?](wkwebextensioncontext/overridenewtabpageurl.md)
  The URL to use as an alternative to the default new tab page, if the extension has one.
- [var uniqueIdentifier: String](wkwebextensioncontext/uniqueidentifier.md)
  A unique identifier used to distinguish the extension from other extensions and target it for messages.
- [var unsupportedAPIs: Set<String>!](wkwebextensioncontext/unsupportedapis.md)
  Specifies unsupported APIs for this extension, making them `undefined` in JavaScript.
- [var webExtension: WKWebExtension](wkwebextensioncontext/webextension.md)
  The extension this context represents.
- [var webExtensionController: WKWebExtensionController?](wkwebextensioncontext/webextensioncontroller.md)
  The extension controller this context is loaded in, otherwise `nil` if it isn’t loaded.
- [var webViewConfiguration: WKWebViewConfiguration?](wkwebextensioncontext/webviewconfiguration.md)
  The web view configuration to use for web views that load pages from this extension.
### Instance Methods
- [func action(for: (any WKWebExtensionTab)?) -> WKWebExtension.Action?](wkwebextensioncontext/action(for:).md)
  Retrieves the extension action for a given tab, or the default action if `nil` is passed.
- [func clearUserGesture(in: any WKWebExtensionTab)](wkwebextensioncontext/clearusergesture(in:).md)
  Called by the app to clear a user gesture in a specific tab.
- [func command(for: NSEvent) -> WKWebExtension.Command?](wkwebextensioncontext/command(for:).md)
  Retrieves the command associated with the given event without performing it.
- [func didActivateTab(any WKWebExtensionTab, previousActiveTab: (any WKWebExtensionTab)?)](wkwebextensioncontext/didactivatetab(_:previousactivetab:).md)
  Called by the app when a tab is activated to notify only this specific extension.
- [func didChangeTabProperties(WKWebExtension.TabChangedProperties, for: any WKWebExtensionTab)](wkwebextensioncontext/didchangetabproperties(_:for:).md)
  Called by the app when the properties of a tab are changed to fire appropriate events with only this extension.
- [func didCloseTab(any WKWebExtensionTab, windowIsClosing: Bool)](wkwebextensioncontext/didclosetab(_:windowisclosing:).md)
  Called by the app when a tab is closed to fire appropriate events with only this extension.
- [func didCloseWindow(any WKWebExtensionWindow)](wkwebextensioncontext/didclosewindow(_:).md)
  Called by the app when a window is closed to fire appropriate events with only this extension.
- [func didDeselectTabs([any WKWebExtensionTab])](wkwebextensioncontext/diddeselecttabs(_:).md)
  Called by the app when tabs are deselected to fire appropriate events with only this extension.
- [func didFocusWindow((any WKWebExtensionWindow)?)](wkwebextensioncontext/didfocuswindow(_:).md)
  Called by the app when a window gains focus to fire appropriate events with only this extension.
- [func didMoveTab(any WKWebExtensionTab, from: Int, in: (any WKWebExtensionWindow)?)](wkwebextensioncontext/didmovetab(_:from:in:).md)
  Called by the app when a tab is moved to fire appropriate events with only this extension.
- [func didOpenTab(any WKWebExtensionTab)](wkwebextensioncontext/didopentab(_:).md)
  Called by the app when a new tab is opened to fire appropriate events with only this extension.
- [func didOpenWindow(any WKWebExtensionWindow)](wkwebextensioncontext/didopenwindow(_:).md)
  Called by the app when a new window is opened to fire appropriate events with only this extension.
- [func didReplaceTab(any WKWebExtensionTab, with: any WKWebExtensionTab)](wkwebextensioncontext/didreplacetab(_:with:).md)
  Called by the app when a tab is replaced by another tab to fire appropriate events with only this extension.
- [func didSelectTabs([any WKWebExtensionTab])](wkwebextensioncontext/didselecttabs(_:).md)
  Called by the app when tabs are selected to fire appropriate events with only this extension.
- [func hasAccess(to: URL) -> Bool](wkwebextensioncontext/hasaccess(to:).md)
  Checks the specified URL against the currently granted permission match patterns.
- [func hasAccess(to: URL, in: (any WKWebExtensionTab)?) -> Bool](wkwebextensioncontext/hasaccess(to:in:).md)
  Checks the specified URL against the currently granted permission match patterns in a specific tab.
- [func hasActiveUserGesture(in: any WKWebExtensionTab) -> Bool](wkwebextensioncontext/hasactiveusergesture(in:).md)
  Indicates if a user gesture is currently active in the specified tab.
- [func hasInjectedContent(for: URL) -> Bool](wkwebextensioncontext/hasinjectedcontent(for:).md)
  Checks if the extension has script or stylesheet content that can be injected into the specified URL.
- [func hasPermission(WKWebExtension.Permission) -> Bool](wkwebextensioncontext/haspermission(_:).md)
  Checks the specified permission against the currently granted permissions.
- [func hasPermission(WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> Bool](wkwebextensioncontext/haspermission(_:in:).md)
  Checks the specified permission against the currently granted permissions in a specific tab.
- [func loadBackgroundContent(completionHandler: ((any Error)?) -> Void)](wkwebextensioncontext/loadbackgroundcontent(completionhandler:).md)
  Loads the background content if needed for the extension.
- [func menuItems(for: any WKWebExtensionTab) -> [UIMenuElement]](wkwebextensioncontext/menuitems(for:).md)
  Retrieves the menu items for a given tab.
- [func performAction(for: (any WKWebExtensionTab)?)](wkwebextensioncontext/performaction(for:).md)
  Performs the extension action associated with the specified tab or performs the default action if `nil` is passed.
- [func performCommand(WKWebExtension.Command)](wkwebextensioncontext/performcommand(_:).md)
  Performs the specified command, triggering events specific to this extension.
- [func performCommand(for: UIKeyCommand) -> Bool](wkwebextensioncontext/performcommand(for:)-25rd1.md)
  Performs the command associated with the given key command.
- [func performCommand(for: NSEvent) -> Bool](wkwebextensioncontext/performcommand(for:)-8btj0.md)
  Performs the command associated with the given event.
- [func permissionStatus(for: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:)-3qq2w.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func permissionStatus(for: WKWebExtension.MatchPattern) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:)-7mu8.md)
  Checks the specified match pattern against the currently denied, granted, and requested permission match patterns.
- [func permissionStatus(for: URL) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:)-7ojrb.md)
  Checks the specified URL against the currently denied, granted, and requested permission match patterns.
- [func permissionStatus(for: WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:in:)-4h82n.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func permissionStatus(for: URL, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:in:)-96xaf.md)
  Checks the specified URL against the currently denied, granted, and requested permission match patterns.
- [func permissionStatus(for: WKWebExtension.MatchPattern, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:in:)-nqhm.md)
  Checks the specified match pattern against the currently denied, granted, and requested permission match patterns.
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.Permission)](wkwebextensioncontext/setpermissionstatus(_:for:)-4u95f.md)
  Sets the status of a permission with a distant future expiration date.
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: URL)](wkwebextensioncontext/setpermissionstatus(_:for:)-5xahd.md)
  Sets the permission status of a URL with a distant future expiration date.
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.MatchPattern)](wkwebextensioncontext/setpermissionstatus(_:for:)-6auqv.md)
  Sets the status of a match pattern with a distant future expiration date.
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: URL, expirationDate: Date?)](wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-5q9id.md)
  Sets the permission status of a URL with a distant future expiration date.
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.Permission, expirationDate: Date?)](wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-692ui.md)
  Sets the status of a permission with a specific expiration date.
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.MatchPattern, expirationDate: Date?)](wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-7038f.md)
  Sets the status of a match pattern with a specific expiration date.
- [func userGesturePerformed(in: any WKWebExtensionTab)](wkwebextensioncontext/usergestureperformed(in:).md)
  Should be called by the app when a user gesture is performed in a specific tab.

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

- [class WKWebExtension](wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionController](wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext)*