# VSSubscriptionAccessLevel

**Framework**: Video Subscriber Account  
**Kind**: enum

Constants representing a subscriber’s level of access to your content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS ?+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum VSSubscriptionAccessLevel
```

## Topics

### Subscription Tiers
- [VSSubscriptionAccessLevel.freeWithAccount](vssubscriptionaccesslevel/freewithaccount.md)
  The user has access to free content with a valid account.
- [VSSubscriptionAccessLevel.paid](vssubscriptionaccesslevel/paid.md)
  The user has access to content that requires a paid subscription.
- [VSSubscriptionAccessLevel.unknown](vssubscriptionaccesslevel/unknown.md)
  The default access level.
### Initializers
- [init?(rawValue: Int)](vssubscriptionaccesslevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var accessLevel: VSSubscriptionAccessLevel](vssubscription/accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [var billingIdentifier: String?](vssubscription/billingidentifier.md)
  The subscriber’s billing group.
- [var expirationDate: Date!](vssubscription/expirationdate.md)
  The date when the user’s subscription expires.
- [var tierIdentifiers: [String]!](vssubscription/tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionaccesslevel)*