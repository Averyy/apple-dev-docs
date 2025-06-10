# download(_:willPerformHTTPRedirection:newRequest:decisionHandler:)

**Framework**: WebKit  
**Kind**: method

Asks the delegate to respond to the download’s redirect response.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func download(_ download: WKDownload, decidedPolicyForHTTPRedirection response: HTTPURLResponse, newRequest request: URLRequest) async -> WKDownload.RedirectPolicy
```

#### Discussion

Determine whether to proceed with the redirect. Then invoke the decisionHandler closure, providing a download redirect policy that indicates whether to proceed with the redirect.

If you don’t implement this method, the web view proceeds with all redirects.

## Parameters

- `download`: The download that receives the redirect response.
- `response`: The redirect response.
- `request`: The new request the web view sends as a result of the redirect response.
- `decisionHandler`: A closure you must invoke, providing a download redirect policy that indicates whether to proceed with the redirect.

## See Also

- [WKDownload.RedirectPolicy](wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/download(_:willperformhttpredirection:newrequest:decisionhandler:))*