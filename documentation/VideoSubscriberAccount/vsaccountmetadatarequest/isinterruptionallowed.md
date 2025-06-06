# isInterruptionAllowed

**Framework**: Videosubscriberaccount  
**Kind**: property

A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isInterruptionAllowed: Bool { get set }
```

## See Also

- [var featuredAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/featuredaccountprovideridentifiers.md)
  The providers your app lists prominently during authentication.
- [var forceAuthentication: Bool](vsaccountmetadatarequest/forceauthentication.md)
  A Boolean value that indicates whether the app ignores cached credentials.
- [var localizedVideoTitle: String?](vsaccountmetadatarequest/localizedvideotitle.md)
  A short, user-presentable name for the video that the user wants to play.
- [var applicationAccountProviders: [VSAccountApplicationProvider]?](vsaccountmetadatarequest/applicationaccountproviders.md)
  An array of application-specific providers to add to the list of account providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/isinterruptionallowed)*