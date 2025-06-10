# tierIdentifiers

**Framework**: Video Subscriber Account  
**Kind**: property

A list of content from your catalog that the subscriber can access.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS ?+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var tierIdentifiers: [String]! { get set }
```

#### Discussion

You should only use values that are in your availability feed’s tier restrictions.

## See Also

- [var accessLevel: VSSubscriptionAccessLevel](vssubscription/accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [enum VSSubscriptionAccessLevel](vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var billingIdentifier: String?](vssubscription/billingidentifier.md)
  The subscriber’s billing group.
- [var expirationDate: Date!](vssubscription/expirationdate.md)
  The date when the user’s subscription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/tieridentifiers)*