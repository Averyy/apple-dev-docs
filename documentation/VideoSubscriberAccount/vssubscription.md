# VSSubscription

**Framework**: Videosubscriberaccount  
**Kind**: class

An object that describes a subscriber’s access to content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VSSubscriptionRegistrationCenter](vssubscriptionregistrationcenter.md)
  An object that stores subscription information that the system provides to the Apple TV app.
- [class VSAccountApplicationProvider](vsaccountapplicationprovider.md)
  An object to display app-specific providers in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription)*