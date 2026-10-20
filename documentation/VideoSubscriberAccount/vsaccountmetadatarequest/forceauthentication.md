# forceAuthentication

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app ignores cached credentials.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var forceAuthentication: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL forceAuthentication;
```

#### Discussion

If [`true`](../../Swift/true.md), your app cannot use cached credentials; if [`false`](../../Swift/false.md), your app attempts to use any available cached credentials.

## See Also

### Specifying Additional Options
- [var isInterruptionAllowed: Bool](./isinterruptionallowed.md)
  A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.
- [var featuredAccountProviderIdentifiers: [String]](./featuredaccountprovideridentifiers.md)
  The providers your app lists prominently during authentication.
- [var localizedVideoTitle: String?](./localizedvideotitle.md)
  A short, user-presentable name for the video that the user wants to play.
- [var applicationAccountProviders: [VSAccountApplicationProvider]?](./applicationaccountproviders.md)
  An array of application-specific providers to add to the list of account providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/forceauthentication)*