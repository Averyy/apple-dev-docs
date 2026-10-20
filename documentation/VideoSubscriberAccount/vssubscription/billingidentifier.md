# billingIdentifier

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The subscriber’s billing group.

**Availability**:
- iOS 11.3+ - Deprecated in 18.0
- iPadOS 11.3+ - Deprecated in 18.0
- Mac Catalyst 11.3+ - Deprecated in 18.0
- macOS
- tvOS 11.3+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
var billingIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * billingIdentifier;
```

#### Discussion

You can use this property to restrict content availability based on the proximity of the billing address to a specific venue.

## See Also

### Setting Subscription Details
- [var accessLevel: VSSubscriptionAccessLevel](./accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [enum VSSubscriptionAccessLevel](../vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var expirationDate: Date!](./expirationdate.md)
  The date when the user’s subscription expires.
- [var tierIdentifiers: [String]!](./tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/billingidentifier)*