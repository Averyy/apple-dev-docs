# cancel(_:)

**Framework**: WebKit  
**Kind**: method

Cancels the download, and optionally captures data so that you can resume the download later.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cancel() async -> Data?
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func cancel() async -> Data?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A closure you provide to capture and store data so that you can resume the download later.

## See Also

- [var delegate: (any WKDownloadDelegate)?](wkdownload/delegate.md)
  An object you use to track download progress and handle redirects, authentication challenges, and failures.
- [WKDownload.RedirectPolicy](wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/cancel(_:))*