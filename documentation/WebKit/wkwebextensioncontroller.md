# WKWebExtensionController

**Framework**: Webkit  
**Kind**: class

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

#### Overview

You can have one or more extension controller instances, allowing different parts of the app to use different sets of extensions.

You can associate a controller with [`WKWebView`](wkwebview.md) using the [`webExtensionController`](wkwebviewconfiguration/webextensioncontroller.md) property on [`WKWebViewConfiguration`](wkwebviewconfiguration.md).

## Topics

### Initializers
- [init()](wkwebextensioncontroller/init.md)
  Returns a web extension controller initialized with the default configuration.
- [init(configuration: WKWebExtensionController.Configuration)](wkwebextensioncontroller/init(configuration:).md)
  Returns a web extension controller initialized with the specified configuration.
### Instance Properties
- [var configuration: WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.property.md)
  A copy of the configuration with which the web extension controller was initialized.
- [var delegate: (any WKWebExtensionControllerDelegate)?](wkwebextensioncontroller/delegate.md)
  The extension controller delegate.
- [var extensionContexts: Set<WKWebExtensionContext>](wkwebextensioncontroller/extensioncontexts.md)
  A set of all the currently loaded extension contexts.
- [var extensions: Set<WKWebExtension>](wkwebextensioncontroller/extensions.md)
  A set of all the currently loaded extensions.
### Instance Methods
- [func didActivateTab(any WKWebExtensionTab, previousActiveTab: (any WKWebExtensionTab)?)](wkwebextensioncontroller/didactivatetab(_:previousactivetab:).md)
  Should be called by the app when a tab is activated to notify all loaded web extensions.
- [func didChangeTabProperties(WKWebExtension.TabChangedProperties, for: any WKWebExtensionTab)](wkwebextensioncontroller/didchangetabproperties(_:for:).md)
  Should be called by the app when the properties of a tab are changed to fire appropriate events with all loaded web extensions.
- [func didCloseTab(any WKWebExtensionTab, windowIsClosing: Bool)](wkwebextensioncontroller/didclosetab(_:windowisclosing:).md)
  Should be called by the app when a tab is closed to fire appropriate events with all loaded web extensions.
- [func didCloseWindow(any WKWebExtensionWindow)](wkwebextensioncontroller/didclosewindow(_:).md)
  Should be called by the app when a window is closed to fire appropriate events with all loaded web extensions.
- [func didDeselectTabs([any WKWebExtensionTab])](wkwebextensioncontroller/diddeselecttabs(_:).md)
  Should be called by the app when tabs are deselected to fire appropriate events with all loaded web extensions.
- [func didFocusWindow((any WKWebExtensionWindow)?)](wkwebextensioncontroller/didfocuswindow(_:).md)
  Should be called by the app when a window gains focus to fire appropriate events with all loaded web extensions.
- [func didMoveTab(any WKWebExtensionTab, from: Int, in: (any WKWebExtensionWindow)?)](wkwebextensioncontroller/didmovetab(_:from:in:).md)
  Should be called by the app when a tab is moved to fire appropriate events with all loaded web extensions.
- [func didOpenTab(any WKWebExtensionTab)](wkwebextensioncontroller/didopentab(_:).md)
  Should be called by the app when a new tab is opened to fire appropriate events with all loaded web extensions.
- [func didOpenWindow(any WKWebExtensionWindow)](wkwebextensioncontroller/didopenwindow(_:).md)
  Should be called by the app when a new window is opened to fire appropriate events with all loaded web extensions.
- [func didReplaceTab(any WKWebExtensionTab, with: any WKWebExtensionTab)](wkwebextensioncontroller/didreplacetab(_:with:).md)
  Should be called by the app when a tab is replaced by another tab to fire appropriate events with all loaded web extensions.
- [func didSelectTabs([any WKWebExtensionTab])](wkwebextensioncontroller/didselecttabs(_:).md)
  Should be called by the app when tabs are selected to fire appropriate events with all loaded web extensions.
- [func extensionContext(for: URL) -> WKWebExtensionContext?](wkwebextensioncontroller/extensioncontext(for:)-2kr4.md)
  Returns a loaded extension context matching the specified URL.
- [func extensionContext(for: WKWebExtension) -> WKWebExtensionContext?](wkwebextensioncontroller/extensioncontext(for:)-6ecpm.md)
  Returns a loaded extension context for the specified extension.
- [func fetchDataRecord(ofTypes: Set<WKWebExtension.DataType>, for: WKWebExtensionContext, completionHandler: (WKWebExtension.DataRecord?) -> Void)](wkwebextensioncontroller/fetchdatarecord(oftypes:for:completionhandler:).md)
  Fetches a data record containing the given extension data types for a specific known web extension context.
- [func fetchDataRecords(ofTypes: Set<WKWebExtension.DataType>, completionHandler: ([WKWebExtension.DataRecord]) -> Void)](wkwebextensioncontroller/fetchdatarecords(oftypes:completionhandler:).md)
  Fetches data records containing the given extension data types for all known extensions.
- [func load(WKWebExtensionContext) throws](wkwebextensioncontroller/load(_:).md)
  Loads the specified extension context.
- [func removeData(ofTypes: Set<WKWebExtension.DataType>, from: [WKWebExtension.DataRecord], completionHandler: () -> Void)](wkwebextensioncontroller/removedata(oftypes:from:completionhandler:).md)
  Removes extension data of the given types for the given data records.
- [func unload(WKWebExtensionContext) throws](wkwebextensioncontroller/unload(_:).md)
  Unloads the specified extension context.
### Type Properties
- [class var allExtensionDataTypes: Set<WKWebExtension.DataType>](wkwebextensioncontroller/allextensiondatatypes.md)
  Returns a set of all available extension data types.

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
- [class WKWebExtensionContext](wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [protocol WKWebExtensionControllerDelegate](wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller)*