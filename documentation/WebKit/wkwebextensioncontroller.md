# WKWebExtensionController

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

An object that manages a set of loaded extension contexts.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class WKWebExtensionController
```

```objc
@interface WKWebExtensionController : NSObject
```

## Overview

You can have one or more extension controller instances, allowing different parts of the app to use different sets of extensions.

You can associate a controller with [`WKWebView`](./wkwebview.md) using the [`webExtensionController`](./wkwebviewconfiguration/webextensioncontroller.md) property on [`WKWebViewConfiguration`](./wkwebviewconfiguration.md).

## Topics

### Initializers
- [init()](./wkwebextensioncontroller/init%28%29.md)
  Returns a web extension controller initialized with the default configuration.
- [init(configuration: WKWebExtensionController.Configuration)](./wkwebextensioncontroller/init%28configuration%29.md)
  Returns a web extension controller initialized with the specified configuration.
### Instance Properties
- [var configuration: WKWebExtensionController.Configuration](./wkwebextensioncontroller/configuration-swift.property.md)
  A copy of the configuration with which the web extension controller was initialized.
- [var delegate: (any WKWebExtensionControllerDelegate)?](./wkwebextensioncontroller/delegate.md)
  The extension controller delegate.
- [var extensionContexts: Set<WKWebExtensionContext>](./wkwebextensioncontroller/extensioncontexts.md)
  A set of all the currently loaded extension contexts.
- [var extensions: Set<WKWebExtension>](./wkwebextensioncontroller/extensions.md)
  A set of all the currently loaded extensions.
### Instance Methods
- [func didActivateTab(any WKWebExtensionTab, previousActiveTab: (any WKWebExtensionTab)?)](./wkwebextensioncontroller/didactivatetab%28_,previousactivetab%29.md)
  Should be called by the app when a tab is activated to notify all loaded web extensions.
- [func didChangeTabProperties(WKWebExtension.TabChangedProperties, for: any WKWebExtensionTab)](./wkwebextensioncontroller/didchangetabproperties%28_,for%29.md)
  Should be called by the app when the properties of a tab are changed to fire appropriate events with all loaded web extensions.
- [func didCloseTab(any WKWebExtensionTab, windowIsClosing: Bool)](./wkwebextensioncontroller/didclosetab%28_,windowisclosing%29.md)
  Should be called by the app when a tab is closed to fire appropriate events with all loaded web extensions.
- [func didCloseWindow(any WKWebExtensionWindow)](./wkwebextensioncontroller/didclosewindow%28_%29.md)
  Should be called by the app when a window is closed to fire appropriate events with all loaded web extensions.
- [func didDeselectTabs([any WKWebExtensionTab])](./wkwebextensioncontroller/diddeselecttabs%28_%29.md)
  Should be called by the app when tabs are deselected to fire appropriate events with all loaded web extensions.
- [func didFocusWindow((any WKWebExtensionWindow)?)](./wkwebextensioncontroller/didfocuswindow%28_%29.md)
  Should be called by the app when a window gains focus to fire appropriate events with all loaded web extensions.
- [func didMoveTab(any WKWebExtensionTab, from: Int, in: (any WKWebExtensionWindow)?)](./wkwebextensioncontroller/didmovetab%28_,from,in%29.md)
  Should be called by the app when a tab is moved to fire appropriate events with all loaded web extensions.
- [func didOpenTab(any WKWebExtensionTab)](./wkwebextensioncontroller/didopentab%28_%29.md)
  Should be called by the app when a new tab is opened to fire appropriate events with all loaded web extensions.
- [func didOpenWindow(any WKWebExtensionWindow)](./wkwebextensioncontroller/didopenwindow%28_%29.md)
  Should be called by the app when a new window is opened to fire appropriate events with all loaded web extensions.
- [func didReplaceTab(any WKWebExtensionTab, with: any WKWebExtensionTab)](./wkwebextensioncontroller/didreplacetab%28_,with%29.md)
  Should be called by the app when a tab is replaced by another tab to fire appropriate events with all loaded web extensions.
- [func didSelectTabs([any WKWebExtensionTab])](./wkwebextensioncontroller/didselecttabs%28_%29.md)
  Should be called by the app when tabs are selected to fire appropriate events with all loaded web extensions.
- [func extensionContext(for: URL) -> WKWebExtensionContext?](./wkwebextensioncontroller/extensioncontext%28for%29-2kr4.md)
  Returns a loaded extension context matching the specified URL.
- [func extensionContext(for: WKWebExtension) -> WKWebExtensionContext?](./wkwebextensioncontroller/extensioncontext%28for%29-6ecpm.md)
  Returns a loaded extension context for the specified extension.
- [func fetchDataRecord(ofTypes: Set<WKWebExtension.DataType>, for: WKWebExtensionContext, completionHandler: (WKWebExtension.DataRecord?) -> Void)](./wkwebextensioncontroller/fetchdatarecord%28oftypes,for,completionhandler%29.md)
  Fetches a data record containing the given extension data types for a specific known web extension context.
- [func fetchDataRecords(ofTypes: Set<WKWebExtension.DataType>, completionHandler: ([WKWebExtension.DataRecord]) -> Void)](./wkwebextensioncontroller/fetchdatarecords%28oftypes,completionhandler%29.md)
  Fetches data records containing the given extension data types for all known extensions.
- [func load(WKWebExtensionContext) throws](./wkwebextensioncontroller/load%28_%29.md)
  Loads the specified extension context.
- [func removeData(ofTypes: Set<WKWebExtension.DataType>, from: [WKWebExtension.DataRecord], completionHandler: () -> Void)](./wkwebextensioncontroller/removedata%28oftypes,from,completionhandler%29.md)
  Removes extension data of the given types for the given data records.
- [func unload(WKWebExtensionContext) throws](./wkwebextensioncontroller/unload%28_%29.md)
  Unloads the specified extension context.
- [- didActivateTab:previousActiveTab:](./wkwebextensioncontroller/didactivatetab_previousactivetab_.md)
  Should be called by the app when a tab is activated to notify all loaded web extensions.
- [- didCloseTab:windowIsClosing:](./wkwebextensioncontroller/didclosetab_windowisclosing_.md)
  Should be called by the app when a tab is closed to fire appropriate events with all loaded web extensions.
- [- didMoveTab:fromIndex:inWindow:](./wkwebextensioncontroller/didmovetab_fromindex_inwindow_.md)
  Should be called by the app when a tab is moved to fire appropriate events with all loaded web extensions.
### Type Properties
- [class var allExtensionDataTypes: Set<WKWebExtension.DataType>](./wkwebextensioncontroller/allextensiondatatypes.md)
  Returns a set of all available extension data types.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Web extensions
- [class WKWebExtension](./wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](./wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](./wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](./wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [protocol WKWebExtensionControllerDelegate](./wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.
- [WKWebExtension.Action](./wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](./wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.MatchPattern](./wkwebextension/matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](./wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.DataRecord](./wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](./wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](./wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](./wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](./wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller)*