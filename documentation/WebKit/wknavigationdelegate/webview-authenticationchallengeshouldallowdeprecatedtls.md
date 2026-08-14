# webView(_:authenticationChallenge:shouldAllowDeprecatedTLS:)

**Framework**: WebKit  
**Kind**: method

Asks the delegate whether to continue with a connection that uses a deprecated version of TLS.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, shouldAllowDeprecatedTLSFor challenge: URLAuthenticationChallenge) async -> Bool
```

#### Discussion

If you don’t implement this method, the web view uses system settings to determine whether to allow the use of deprecated versions of TLS.

## Parameters

- `webView`: The web view that receives the authentication challenge.
- `challenge`: The authentication challenge.
- `decisionHandler`: The completion handler block to execute with the decision. This handler has no return value and takes the following parameter: - **decision**: A Boolean value that indicates whether to continue to use a deprecated version of TLS. Specify [`true`](https://developer.apple.com/documentation/swift/true) to continue, or [`false`](https://developer.apple.com/documentation/swift/false) to reject the connection.

## See Also

- [func webView(WKWebView, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](wknavigationdelegate/webview(_:didreceive:completionhandler:).md)
  Asks the delegate to respond to an authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:authenticationchallenge:shouldallowdeprecatedtls:))*