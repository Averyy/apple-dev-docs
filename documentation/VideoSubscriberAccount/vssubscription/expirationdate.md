# expirationDate

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The date when the user’s subscription expires.

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
var expirationDate: Date! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSDate * expirationDate;
```

## Discussion

This property defines the exact time when the subscription becomes inactive. When the current subscription becomes inactive, the system behaves as though the person isn’t a subscriber, similar to calling [`setCurrentSubscription(_:)`](../vssubscriptionregistrationcenter/setcurrentsubscription%28_%29.md) with a value of `nil`.

You can use this property when a subscriber decides not to renew their subscription by setting an expiration date that corresponds to the final billing cycle end date.

You can also use this property when a subscription only grants access to time-limited content, such as a single season of games for a sports league.

The default is `distantFuture`.

## See Also

### Setting Subscription Details
- [var accessLevel: VSSubscriptionAccessLevel](./accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [enum VSSubscriptionAccessLevel](../vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var billingIdentifier: String?](./billingidentifier.md)
  The subscriber’s billing group.
- [var tierIdentifiers: [String]!](./tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/expirationdate)*