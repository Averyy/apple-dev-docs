# WKDownload.RedirectPolicy

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum WKDownloadRedirectPolicy : NSInteger;
```

## Topics

### Constants
- [WKDownload.RedirectPolicy.allow](./redirectpolicy/allow.md)
  Allow a redirect to proceed.
- [WKDownload.RedirectPolicy.cancel](./redirectpolicy/cancel.md)
  Cancel the redirect action.
### Initializers
- [init?(rawValue: Int)](./redirectpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the download
- [var delegate: (any WKDownloadDelegate)?](./delegate.md)
  An object you use to track download progress and handle redirects, authentication challenges, and failures.
- [func cancel(((Data?) -> Void)?)](./cancel%28_%29.md)
  Cancels the download, and optionally captures data so that you can resume the download later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/redirectpolicy)*