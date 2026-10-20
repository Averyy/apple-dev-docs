# WKWebExtension.MatchPattern

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

An object that represents a way to specify groups of URLs.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class MatchPattern
```

```objc
@interface WKWebExtensionMatchPattern : NSObject
```

#### Overview

All match patterns are specified as strings. Apart from the special `<all_urls>` pattern, match patterns consist of three parts: scheme, host, and path.

## Topics

### Errors
- [WKWebExtension.MatchPattern.Error](./matchpattern/error.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](./matchpattern.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](./matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](./matchpattern.md) domain.
- [class let errorDomain: String](./matchpattern/errordomain.md)
  A string that identifies the error domain.
### Structures
- [WKWebExtension.MatchPattern.Options](./matchpattern/options.md)
  Constants used by [`WKWebExtension.MatchPattern`](./matchpattern.md) to indicate matching options.
### Initializers
- [init?(coder: NSCoder)](./matchpattern/init%28coder%29.md)
- [init(scheme: String, host: String, path: String) throws](./matchpattern/init%28scheme,host,path%29.md)
  Returns a pattern object for the specified scheme, host, and path strings.
- [init(string: String) throws](./matchpattern/init%28string%29.md)
  Returns a pattern object for the specified pattern string.
### Instance Properties
- [var host: String?](./matchpattern/host.md)
  The host part of the pattern string, unless [`matchesAllURLs`](./matchpattern/matchesallurls.md) is `YES`.
- [var matchesAllHosts: Bool](./matchpattern/matchesallhosts.md)
  A Boolean value that indicates if the pattern is `<all_urls>` or has `*` as the host.
- [var matchesAllURLs: Bool](./matchpattern/matchesallurls.md)
  A Boolean value that indicates if the pattern is `<all_urls>`.
- [var path: String?](./matchpattern/path.md)
  The path part of the pattern string, unless [`matchesAllURLs`](./matchpattern/matchesallurls.md) is `YES`.
- [var scheme: String?](./matchpattern/scheme.md)
  The scheme part of the pattern string, unless [`matchesAllURLs`](./matchpattern/matchesallurls.md) is `YES`.
- [var string: String](./matchpattern/string.md)
  The original pattern string.
### Instance Methods
- [func matches(URL?) -> Bool](./matchpattern/matches%28_%29-471rf.md)
  Matches the receiver pattern against the specified URL.
- [func matches(WKWebExtension.MatchPattern?) -> Bool](./matchpattern/matches%28_%29-4d84f.md)
  Matches the receiver pattern against the specified pattern.
- [func matches(URL?, options: WKWebExtension.MatchPattern.Options) -> Bool](./matchpattern/matches%28_,options%29-5wo3g.md)
  Matches the receiver pattern against the specified URL with options.
- [func matches(WKWebExtension.MatchPattern?, options: WKWebExtension.MatchPattern.Options) -> Bool](./matchpattern/matches%28_,options%29-fnde.md)
  Matches the receiver pattern against the specified pattern with options.
### Type Methods
- [class func allHostsAndSchemes() -> Self](./matchpattern/allhostsandschemes%28%29.md)
  Returns a pattern object that has `*` for scheme, host, and path.
- [class func allURLs() -> Self](./matchpattern/allurls%28%29.md)
  Returns a pattern object for `<all_urls>`.
- [class func registerCustomURLScheme(String)](./matchpattern/registercustomurlscheme%28_%29.md)
  Registers a custom URL scheme that can be used in match patterns.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Web extensions
- [class WKWebExtension](../wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](../wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](../wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](../wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](../wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](../wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.
- [WKWebExtension.Action](./action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](./command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.MessagePort](./messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.DataRecord](./datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](./tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](./windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](../wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](../wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern)*