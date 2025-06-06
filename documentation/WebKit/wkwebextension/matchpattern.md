# WKWebExtension.MatchPattern

**Framework**: Webkit  
**Kind**: class

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

#### Overview

All match patterns are specified as strings. Apart from the special `<all_urls>` pattern, match patterns consist of three parts: scheme, host, and path.

## Topics

### Errors
- [WKWebExtension.MatchPattern.Error](wkwebextension/matchpattern/error.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [class let errorDomain: String](wkwebextension/matchpattern/errordomain.md)
  A string that identifies the error domain.
### Structures
- [WKWebExtension.MatchPattern.Options](wkwebextension/matchpattern/options.md)
  Constants used by [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) to indicate matching options.
### Initializers
- [init(scheme: String, host: String, path: String) throws](wkwebextension/matchpattern/init(scheme:host:path:).md)
  Returns a pattern object for the specified scheme, host, and path strings.
- [init(string: String) throws](wkwebextension/matchpattern/init(string:).md)
  Returns a pattern object for the specified pattern string.
### Instance Properties
- [var host: String?](wkwebextension/matchpattern/host.md)
  The host part of the pattern string, unless [`matchesAllURLs`](wkwebextension/matchpattern/matchesallurls.md) is `YES`.
- [var matchesAllHosts: Bool](wkwebextension/matchpattern/matchesallhosts.md)
  A Boolean value that indicates if the pattern is `<all_urls>` or has `*` as the host.
- [var matchesAllURLs: Bool](wkwebextension/matchpattern/matchesallurls.md)
  A Boolean value that indicates if the pattern is `<all_urls>`.
- [var path: String?](wkwebextension/matchpattern/path.md)
  The path part of the pattern string, unless [`matchesAllURLs`](wkwebextension/matchpattern/matchesallurls.md) is `YES`.
- [var scheme: String?](wkwebextension/matchpattern/scheme.md)
  The scheme part of the pattern string, unless [`matchesAllURLs`](wkwebextension/matchpattern/matchesallurls.md) is `YES`.
- [var string: String](wkwebextension/matchpattern/string.md)
  The original pattern string.
### Instance Methods
- [func matches(URL?) -> Bool](wkwebextension/matchpattern/matches(_:)-471rf.md)
  Matches the receiver pattern against the specified URL.
- [func matches(WKWebExtension.MatchPattern?) -> Bool](wkwebextension/matchpattern/matches(_:)-4d84f.md)
  Matches the receiver pattern against the specified pattern.
- [func matches(URL?, options: WKWebExtension.MatchPattern.Options) -> Bool](wkwebextension/matchpattern/matches(_:options:)-5wo3g.md)
  Matches the receiver pattern against the specified URL with options.
- [func matches(WKWebExtension.MatchPattern?, options: WKWebExtension.MatchPattern.Options) -> Bool](wkwebextension/matchpattern/matches(_:options:)-fnde.md)
  Matches the receiver pattern against the specified pattern with options.
### Type Methods
- [class func allHostsAndSchemes() -> Self](wkwebextension/matchpattern/allhostsandschemes.md)
  Returns a pattern object that has `*` for scheme, host, and path.
- [class func allURLs() -> Self](wkwebextension/matchpattern/allurls.md)
  Returns a pattern object for `<all_urls>`.
- [class func registerCustomURLScheme(String)](wkwebextension/matchpattern/registercustomurlscheme(_:).md)
  Registers a custom URL scheme that can be used in match patterns.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [WKWebExtension.Action](wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.DataRecord](wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.MessagePort](wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.TabConfiguration](wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern)*