# billingIdentifier

**Framework**: Video Subscriber Account  
**Kind**: property

The subscriber’s billing group.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- macOS ?+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var billingIdentifier: String? { get set }
```

#### Discussion

You can use this property to restrict content availability based on the proximity of the billing address to a specific venue.

## See Also

- [var accessLevel: VSSubscriptionAccessLevel](vssubscription/accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [enum VSSubscriptionAccessLevel](vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var expirationDate: Date!](vssubscription/expirationdate.md)
  The date when the user’s subscription expires.
- [var tierIdentifiers: [String]!](vssubscription/tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/billingidentifier)*