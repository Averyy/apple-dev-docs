# localizedVideoTitle

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A short, user-presentable name for the video that the user wants to play.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var localizedVideoTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * localizedVideoTitle;
```

## Discussion

Use this property to display a short localized name for the video your app will play if the request is successful. For example, `My Cool Movie` or `My Favorite Show S2 E5`.

A value is not required if your app isn’t sending the request to play a specific video.

## See Also

### Specifying Additional Options
- [var isInterruptionAllowed: Bool](./isinterruptionallowed.md)
  A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.
- [var featuredAccountProviderIdentifiers: [String]](./featuredaccountprovideridentifiers.md)
  The providers your app lists prominently during authentication.
- [var forceAuthentication: Bool](./forceauthentication.md)
  A Boolean value that indicates whether the app ignores cached credentials.
- [var applicationAccountProviders: [VSAccountApplicationProvider]?](./applicationaccountproviders.md)
  An array of application-specific providers to add to the list of account providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/localizedvideotitle)*