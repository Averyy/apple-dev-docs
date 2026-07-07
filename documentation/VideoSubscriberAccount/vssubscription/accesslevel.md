# accessLevel

**Framework**: Video Subscriber Account  
**Kind**: property

The subscriber’s level of access to your catalog of content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS ?+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var accessLevel: VSSubscriptionAccessLevel { get set }
```

#### Discussion

An error occurs if you try to set this property to [`VSSubscriptionAccessLevel.unknown`](vssubscriptionaccesslevel/unknown.md).

## See Also

- [enum VSSubscriptionAccessLevel](vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var billingIdentifier: String?](vssubscription/billingidentifier.md)
  The subscriber’s billing group.
- [var expirationDate: Date!](vssubscription/expirationdate.md)
  The date when the user’s subscription expires.
- [var tierIdentifiers: [String]!](vssubscription/tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/accesslevel)*