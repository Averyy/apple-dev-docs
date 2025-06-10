# value

**Framework**: Video Subscriber Account  
**Kind**: property

A string that represents a person’s account.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var value: String? { get }
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

Your app determines the contents of this property using a mechanism you determine fitting to identify the account. Only your app consumes this property and interprets its contents, for example, by ensuring it represents an account with a valid subscription.

To avoid collisions with other tokens, make the contents of sufficient length and complexity. To validate the contents, you can include a cryptographic signature. For example, see the [`JSON Web Token (JWT)`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519) specification for a standardized authentication method that features these benefits.

On tvOS, if the framework fails to find a token for the current Apple Account, it also checks the system default Apple Account, if different from the current Apple Account. If the default Apple Account also doesn’t have a token, the system stops looking.

> ❗ **Important**: Apple stores the string value to the Apple Account as is; avoid including sensitive information in the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosignintoken-swift.struct/value)*