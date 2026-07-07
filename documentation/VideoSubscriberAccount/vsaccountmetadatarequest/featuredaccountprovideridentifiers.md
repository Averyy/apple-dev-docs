# featuredAccountProviderIdentifiers

**Framework**: Video Subscriber Account  
**Kind**: property

The providers your app lists prominently during authentication.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS ?+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var featuredAccountProviderIdentifiers: [String] { get set }
```

#### Discussion

Use this property to specify which providers your app gives prominent placement to when it asks the user to choose an account provider for authentication. By default, no providers are promoted.

## See Also

- [var isInterruptionAllowed: Bool](vsaccountmetadatarequest/isinterruptionallowed.md)
  A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.
- [var forceAuthentication: Bool](vsaccountmetadatarequest/forceauthentication.md)
  A Boolean value that indicates whether the app ignores cached credentials.
- [var localizedVideoTitle: String?](vsaccountmetadatarequest/localizedvideotitle.md)
  A short, user-presentable name for the video that the user wants to play.
- [var applicationAccountProviders: [VSAccountApplicationProvider]?](vsaccountmetadatarequest/applicationaccountproviders.md)
  An array of application-specific providers to add to the list of account providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/featuredaccountprovideridentifiers)*