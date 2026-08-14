# webView(_:didReceive:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Asks the delegate to respond to an authentication challenge.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, respondTo challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

## Mentions

- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)

#### Discussion

If you don’t implement this method, the web view responds to the authentication challenge with the [`URLSession.AuthChallengeDisposition.rejectProtectionSpace`](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/rejectprotectionspace) disposition.

## Parameters

- `webView`: The web view that receives the authentication challenge.
- `challenge`: The authentication challenge.
- `completionHandler`: A completion handler block to execute with the response. This handler has no return value and takes the following parameters: - **disposition**: The option to use to handle the challenge. For a list of options, see [`URLSession.AuthChallengeDisposition`](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition).
- **credential**: The credential to use for authentication when the `disposition` parameter contains the value [`URLSession.AuthChallengeDisposition.useCredential`](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/usecredential). Specify `nil` to continue without a credential.

## See Also

- [func webView(WKWebView, authenticationChallenge: URLAuthenticationChallenge, shouldAllowDeprecatedTLS: (Bool) -> Void)](wknavigationdelegate/webview(_:authenticationchallenge:shouldallowdeprecatedtls:).md)
  Asks the delegate whether to continue with a connection that uses a deprecated version of TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didreceive:completionhandler:))*