# WKDownload

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface WKDownload : NSObject
```

## Topics

### Managing the download
- [var delegate: (any WKDownloadDelegate)?](./wkdownload/delegate.md)
  An object you use to track download progress and handle redirects, authentication challenges, and failures.
- [func cancel(((Data?) -> Void)?)](./wkdownload/cancel%28_%29.md)
  Cancels the download, and optionally captures data so that you can resume the download later.
- [WKDownload.RedirectPolicy](./wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.
### Inspecting the download
- [var originalRequest: URLRequest?](./wkdownload/originalrequest.md)
  An object that represents the request that initiated the download.
- [var webView: WKWebView?](./wkdownload/webview.md)
  The web view where the download initiated.
### Instance Properties
- [var isUserInitiated: Bool](./wkdownload/isuserinitiated.md)
- [var originatingFrame: WKFrameInfo](./wkdownload/originatingframe.md)

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
- [ProgressReporting](../Foundation/progressreporting.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Downloads
- [protocol WKDownloadDelegate](./wkdownloaddelegate.md)
  A protocol you implement to track download progress and handle redirects, authentication challenges, and failures.
- [WKDownload.PlaceholderPolicy](./wkdownload/placeholderpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload)*