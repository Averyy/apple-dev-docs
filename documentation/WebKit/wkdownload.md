# WKDownload

**Framework**: Webkit  
**Kind**: class

An object that represents the download of a web resource.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKDownload
```

## Topics

### Managing the download
- [var delegate: (any WKDownloadDelegate)?](wkdownload/delegate.md)
  An object you use to track download progress and handle redirects, authentication challenges, and failures.
- [func cancel(((Data?) -> Void)?)](wkdownload/cancel(_:).md)
  Cancels the download, and optionally captures data so that you can resume the download later.
- [WKDownload.RedirectPolicy](wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.
### Inspecting the download
- [var originalRequest: URLRequest?](wkdownload/originalrequest.md)
  An object that represents the request that initiated the download.
- [var webView: WKWebView?](wkdownload/webview.md)
  The web view where the download initiated.
### Instance Properties
- [var isUserInitiated: Bool](wkdownload/isuserinitiated.md)
- [var originatingFrame: WKFrameInfo](wkdownload/originatingframe.md)
### Enumerations
- [WKDownload.PlaceholderPolicy](wkdownload/placeholderpolicy.md)

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
- [ProgressReporting](../Foundation/ProgressReporting.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol WKDownloadDelegate](wkdownloaddelegate.md)
  A protocol you implement to track download progress and handle redirects, authentication challenges, and failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload)*