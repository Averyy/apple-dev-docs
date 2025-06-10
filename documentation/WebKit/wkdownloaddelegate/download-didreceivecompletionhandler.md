# download(_:didReceive:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Asks the delegate to respond to an authentication challenge.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func download(_ download: WKDownload, respondTo challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

#### Discussion

Determine how to respond to the authentication challenge in this method. Then invoke `completionHandler` with a disposition that describes how to respond to the authorization challenge, and optional credentials.

If you don’t implement this method, the web view responds to the challenge with [`URLSession.AuthChallengeDisposition.rejectProtectionSpace`](https://developer.apple.com/documentation/Foundation/URLSession/AuthChallengeDisposition/rejectProtectionSpace).

## Parameters

- `download`: The download that received the authentication challenge.
- `challenge`: The authentication challenge.
- `completionHandler`: A closure you must invoke to respond to the authentication challenge. Provide the closure with a disposition that describes how to respond to the authorization challenge, and optional credentials.

## See Also

- [WKDownload.RedirectPolicy](wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/download(_:didreceive:completionhandler:))*