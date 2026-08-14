# VSSubscription

**Framework**: Video Subscriber Account  
**Kind**: class

An object that describes a subscriber’s access to content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS ?+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VSSubscription
```

#### Overview

Use a `VSSubscription` object to set user subscription information, such as account access type, proximity billing group, expiration date, and content catalog tier identifiers.

## Topics

### Setting Subscription Details
- [var accessLevel: VSSubscriptionAccessLevel](vssubscription/accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [enum VSSubscriptionAccessLevel](vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var billingIdentifier: String?](vssubscription/billingidentifier.md)
  The subscriber’s billing group.
- [var expirationDate: Date!](vssubscription/expirationdate.md)
  The date when the user’s subscription expires.
- [var tierIdentifiers: [String]!](vssubscription/tieridentifiers.md)
  A list of content from your catalog that the subscriber can access.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription)*