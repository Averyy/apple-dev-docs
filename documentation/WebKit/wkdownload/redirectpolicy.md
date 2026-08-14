# WKDownload.RedirectPolicy

**Framework**: WebKit  
**Kind**: enum

An enumeration with cases that indicate whether to proceed with a redirect.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
enum RedirectPolicy
```

## Topics

### Constants
- [WKDownload.RedirectPolicy.allow](wkdownload/redirectpolicy/allow.md)
  Allow a redirect to proceed.
- [WKDownload.RedirectPolicy.cancel](wkdownload/redirectpolicy/cancel.md)
  Cancel the redirect action.
### Initializers
- [init?(rawValue: Int)](wkdownload/redirectpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var delegate: (any WKDownloadDelegate)?](wkdownload/delegate.md)
  An object you use to track download progress and handle redirects, authentication challenges, and failures.
- [func cancel(((Data?) -> Void)?)](wkdownload/cancel(_:).md)
  Cancels the download, and optionally captures data so that you can resume the download later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/redirectpolicy)*