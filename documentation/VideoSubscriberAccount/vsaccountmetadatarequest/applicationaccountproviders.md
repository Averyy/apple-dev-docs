# applicationAccountProviders

**Framework**: Videosubscriberaccount  
**Kind**: property

An array of application-specific providers to add to the list of account providers.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- macOS ?+
- tvOS 14.2+
- visionOS 1.0+

## Declaration

```swift
var applicationAccountProviders: [VSAccountApplicationProvider]? { get set }
```

## See Also

- [var isInterruptionAllowed: Bool](vsaccountmetadatarequest/isinterruptionallowed.md)
  A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.
- [var featuredAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/featuredaccountprovideridentifiers.md)
  The providers your app lists prominently during authentication.
- [var forceAuthentication: Bool](vsaccountmetadatarequest/forceauthentication.md)
  A Boolean value that indicates whether the app ignores cached credentials.
- [var localizedVideoTitle: String?](vsaccountmetadatarequest/localizedvideotitle.md)
  A short, user-presentable name for the video that the user wants to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/applicationaccountproviders)*