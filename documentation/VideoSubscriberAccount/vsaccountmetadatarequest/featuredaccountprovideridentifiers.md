# featuredAccountProviderIdentifiers

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The providers your app lists prominently during authentication.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var featuredAccountProviderIdentifiers: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * featuredAccountProviderIdentifiers;
```

## Discussion

Use this property to specify which providers your app gives prominent placement to when it asks the user to choose an account provider for authentication. By default, no providers are promoted.

## See Also

### Specifying Additional Options
- [var isInterruptionAllowed: Bool](./isinterruptionallowed.md)
  A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.
- [var forceAuthentication: Bool](./forceauthentication.md)
  A Boolean value that indicates whether the app ignores cached credentials.
- [var localizedVideoTitle: String?](./localizedvideotitle.md)
  A short, user-presentable name for the video that the user wants to play.
- [var applicationAccountProviders: [VSAccountApplicationProvider]?](./applicationaccountproviders.md)
  An array of application-specific providers to add to the list of account providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/featuredaccountprovideridentifiers)*