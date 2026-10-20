# delegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An object you use to track download progress and handle redirects, authentication challenges, and failures.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any WKDownloadDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<WKDownloadDelegate> delegate;
```

## See Also

### Managing the download
- [func cancel(((Data?) -> Void)?)](./cancel%28_%29.md)
  Cancels the download, and optionally captures data so that you can resume the download later.
- [WKDownload.RedirectPolicy](./redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/delegate)*