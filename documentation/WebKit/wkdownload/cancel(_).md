# cancel(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Cancels the download, and optionally captures data so that you can resume the download later.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func cancel(_ completionHandler: (@MainActor @Sendable (Data?) -> Void)? = nil)
```

```swift
func cancel() async -> Data?
```

```objc
- (void) cancel:(void (^)(NSData *)) completionHandler;
```

## Parameters

- `completionHandler`: A closure you provide to capture and store data so that you can resume the download later.

## See Also

### Managing the download
- [var delegate: (any WKDownloadDelegate)?](./delegate.md)
  An object you use to track download progress and handle redirects, authentication challenges, and failures.
- [WKDownload.RedirectPolicy](./redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/cancel(_:))*