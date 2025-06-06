# WKWebExtension

**Framework**: Webkit  
**Kind**: class

An object that encapsulates a web extension’s resources that the manifest file defines.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class WKWebExtension
```

#### Overview

This class reads and parses the `manifest.json` file along with the supporting resources like icons and localizations.

## Topics

### Classes
- [WKWebExtension.Action](wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.DataRecord](wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.MatchPattern](wkwebextension/matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.TabConfiguration](wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.
### Structures
- [WKWebExtension.DataType](wkwebextension/datatype.md)
  Constants for specifying data types for a [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md).
- [WKWebExtension.Error](wkwebextension/error.md)
  Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.
- [WKWebExtension.Permission](wkwebextension/permission.md)
  Constants for specifying permission in a [`WKWebExtensionContext`](wkwebextensioncontext.md).
- [WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.
### Enumerations
- [WKWebExtension.WindowState](wkwebextension/windowstate.md)
  Constants used by [`WKWebExtensionWindow`](wkwebextensionwindow.md) to indicate possible states of a window.
- [WKWebExtension.WindowType](wkwebextension/windowtype.md)
  Constants used by [`WKWebExtensionWindow`](wkwebextensionwindow.md) to indicate the type of a window.
### Initializers
- [convenience init(appExtensionBundle: Bundle) async throws](wkwebextension/init(appextensionbundle:).md)
- [convenience init(resourceBaseURL: URL) async throws](wkwebextension/init(resourcebaseurl:).md)
### Instance Properties
- [var allRequestedMatchPatterns: Set<WKWebExtension.MatchPattern>](wkwebextension/allrequestedmatchpatterns.md)
  The set of websites that the extension requires access to for injected content and for receiving messages from websites.
- [var defaultLocale: Locale?](wkwebextension/defaultlocale.md)
  The default locale for the extension.
- [var displayActionLabel: String?](wkwebextension/displayactionlabel.md)
  The default localized extension action label.
- [var displayDescription: String?](wkwebextension/displaydescription.md)
  The localized extension description.
- [var displayName: String?](wkwebextension/displayname.md)
  The localized extension name.
- [var displayShortName: String?](wkwebextension/displayshortname.md)
  The localized extension short name.
- [var displayVersion: String?](wkwebextension/displayversion.md)
  The localized extension display version.
- [var errors: [any Error]](wkwebextension/errors.md)
  An array of all errors that occurred during the processing of the extension.
- [var hasBackgroundContent: Bool](wkwebextension/hasbackgroundcontent.md)
  A Boolean value indicating whether the extension has background content that can run when needed.
- [var hasCommands: Bool](wkwebextension/hascommands.md)
  A Boolean value indicating whether the extension includes commands that users can invoke.
- [var hasContentModificationRules: Bool](wkwebextension/hascontentmodificationrules.md)
  A Boolean value indicating whether the extension includes rules used for content modification or blocking.
- [var hasInjectedContent: Bool](wkwebextension/hasinjectedcontent.md)
  A Boolean value indicating whether the extension has script or stylesheet content that can be injected into webpages.
- [var hasOptionsPage: Bool](wkwebextension/hasoptionspage.md)
  A Boolean value indicating whether the extension has an options page.
- [var hasOverrideNewTabPage: Bool](wkwebextension/hasoverridenewtabpage.md)
  A Boolean value indicating whether the extension provides an alternative to the default new tab page.
- [var hasPersistentBackgroundContent: Bool](wkwebextension/haspersistentbackgroundcontent.md)
  A Boolean value indicating whether the extension has background content that stays in memory as long as the extension is loaded.
- [var manifest: [String : Any]](wkwebextension/manifest.md)
  The parsed manifest as a dictionary.
- [var manifestVersion: Double](wkwebextension/manifestversion.md)
  The parsed manifest version, or `0` if there is no version specified in the manifest.
- [var optionalPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](wkwebextension/optionalpermissionmatchpatterns.md)
  The set of websites that the extension may need access to for optional functionality.
- [var optionalPermissions: Set<WKWebExtension.Permission>](wkwebextension/optionalpermissions.md)
  The set of permissions that the extension may need for optional functionality.
- [var requestedPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](wkwebextension/requestedpermissionmatchpatterns.md)
  The set of websites that the extension requires access to for its base functionality.
- [var requestedPermissions: Set<WKWebExtension.Permission>](wkwebextension/requestedpermissions.md)
  The set of permissions that the extension requires for its base functionality.
- [var version: String?](wkwebextension/version.md)
  The extension version.
### Instance Methods
- [func actionIcon(for: CGSize) -> UIImage?](wkwebextension/actionicon(for:).md)
  Returns the default action icon for the specified size.
- [func icon(for: CGSize) -> UIImage?](wkwebextension/icon(for:).md)
  Returns the extension’s icon image for the specified size.
- [func supportsManifestVersion(Double) -> Bool](wkwebextension/supportsmanifestversion(_:).md)
  Checks if a manifest version is supported by the extension.

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

- [protocol WKWebExtensionTab](wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension)*