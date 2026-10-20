# accessLevel

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The subscriber’s level of access to your catalog of content.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 11.0+ - Deprecated in 18.0
- macOS
- tvOS 11.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use VSUserAccount instead.

## Declaration

```swift
var accessLevel: VSSubscriptionAccessLevel { get set }
```

```objc
@property (nonatomic, assign) VSSubscriptionAccessLevel accessLevel;
```

#### Discussion

An error occurs if you try to set this property to [`VSSubscriptionAccessLevel.unknown`](../vssubscriptionaccesslevel/unknown.md).

## See Also

### Setting Subscription Details
- [enum VSSubscriptionAccessLevel](../vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var billingIdentifier: String?](./billingidentifier.md)
  The subscriber’s billing group.
- [var expirationDate: Date!](./expirationdate.md)
  The date when the user’s subscription expires.
- [var tierIdentifiers: [String]!](./tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/accesslevel)*