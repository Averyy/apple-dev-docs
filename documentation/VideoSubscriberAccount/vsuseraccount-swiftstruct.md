# VSUserAccount

**Framework**: Video Subscriber Account  
**Kind**: struct

An object that represents a user’s account.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+

## Declaration

```swift
struct VSUserAccount
```

#### Overview

There are two sources for a `VSUserAccount` instance:

- You create an instance when a person registers a new account or signs into an existing account in your app, and you call [`update(_:)`](vsuseraccountmanager/update(_:).md) on [`VSUserAccountManager`](vsuseraccountmanager.md) with the instance.
- You fetch user accounts by calling [`userAccounts(options:)`](vsuseraccountmanager/useraccounts(options:).md), which can return user accounts created on the current device, or user accounts registered on all the devices signed into the person’s iCloud account.

## Topics

### Creating user accounts
- [init(accountType: VSUserAccount.AccountType, updateURL: URL?)](vsuseraccount-swift.struct/init(accounttype:updateurl:).md)
  Creates a user account object with a URL for account update requests.
- [VSUserAccount.AccountType](vsuseraccount-swift.struct/accounttype-swift.enum.md)
  Constants that represent whether a user has access to paid content.
### User account information
- [var accountProviderIdentifier: String?](vsuseraccount-swift.struct/accountprovideridentifier.md)
  A string that uniquely identifies a provider known to Apple that provides the user account.
- [var accountType: VSUserAccount.AccountType](vsuseraccount-swift.struct/accounttype-swift.property.md)
  A constant that represents whether a user has access to paid content.
- [var authenticationData: String?](vsuseraccount-swift.struct/authenticationdata.md)
  A string that represents an authentication token for the user account to authenticate with a provider.
- [var billingIdentifier: String?](vsuseraccount-swift.struct/billingidentifier.md)
  A string that Identifies the billing group associated with the user account’s subscription.
- [var deviceCategory: VSUserAccount.OriginatingDeviceCategory](vsuseraccount-swift.struct/devicecategory.md)
  A constant that indicates whether the device from which the user registered is mobile.
- [VSUserAccount.OriginatingDeviceCategory](vsuseraccount-swift.struct/originatingdevicecategory.md)
  Constants that represent whether the device from which the user originally registered is mobile.
- [var identifier: String?](vsuseraccount-swift.struct/identifier.md)
  A string you provide that uniquely identifies the account.
- [var isFromCurrentDevice: Bool](vsuseraccount-swift.struct/isfromcurrentdevice.md)
  A Boolean value that indicates whether the user originated their account on the current device.
- [var isSignedOut: Bool](vsuseraccount-swift.struct/issignedout.md)
  A Boolean value that indicates whether the user has signed out of their account.
- [var requiresSystemTrust: Bool](vsuseraccount-swift.struct/requiressystemtrust.md)
  A Boolean value that indicates whether the update URL must have a system-trusted certificate.
- [var subscriptionBillingCycleEndDate: Date?](vsuseraccount-swift.struct/subscriptionbillingcycleenddate.md)
  A date that indicates when the billing cycle ends for a paid account.
- [var tierIdentifiers: [String]?](vsuseraccount-swift.struct/tieridentifiers.md)
  An array of strings that identify a subset of content from your catalog that the subscriber can play.
- [var updateURL: URL?](vsuseraccount-swift.struct/updateurl.md)
  A URL that points to the application’s JavaScript endpoint for update requests.
### Instance Properties
- [var appleSubscription: VSAppleSubscription?](vsuseraccount-swift.struct/applesubscription.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)
  Implement single sign-on for media-streaming apps by managing a sign-in token on a person’s Apple Account.
- [class VSUserAccountManager](vsuseraccountmanager.md)
  The object that coordinates your app’s user account actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-swift.struct)*