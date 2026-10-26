# VSUserAccount

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

An object that represents a user’s account with a TV provider.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```objc
@interface VSUserAccount : NSObject
```

#### Overview

There are two sources for a `VSUserAccount` instance:

- You create an instance when a person registers a new account or signs into an existing account in your app, and you call [`updateUserAccount:completion:`](./vsuseraccountmanager/updateuseraccount_completion_.md) on [`VSUserAccountManager`](./vsuseraccountmanager.md) with the instance.
- - You fetch user accounts by calling [`queryUserAccountsWithOptions:completion:`](./vsuseraccountmanager/queryuseraccountswithoptions_completion_.md), which can return user accounts created on the current device, or user accounts registered on all the devices signed into the person’s iCloud account.

## Topics

### Creating user accounts
- [- initWithAccountType:updateURL:](./vsuseraccount-c.class/initwithaccounttype_updateurl_.md)
  Creates a user account object with a URL for account update requests.
- [VSUserAccountType](./vsuseraccounttype.md)
  Constants that represent whether a user has access to paid content.
### User account information
- [accountProviderIdentifier](./vsuseraccount-c.class/accountprovideridentifier.md)
  A string that uniquely identifies a TV provider known to Apple that provides the user account.
- [accountType](./vsuseraccount-c.class/accounttype.md)
  A constant that represents whether a user has access to paid content.
- [authenticationData](./vsuseraccount-c.class/authenticationdata.md)
  A string that represents an authentication token for the user account to authenticate with the TV provider.
- [billingIdentifier](./vsuseraccount-c.class/billingidentifier.md)
  A string that Identifies the billing group associated with the user account’s subscription.
- [deviceCategory](./vsuseraccount-c.class/devicecategory.md)
  A constant that indicates whether the device from which the user registered is mobile.
- [VSOriginatingDeviceCategory](./vsoriginatingdevicecategory.md)
  Constants that represent whether the device from which the user originally registered is mobile.
- [fromCurrentDevice](./vsuseraccount-c.class/fromcurrentdevice.md)
  A Boolean value that indicates whether the user originated their account on the current device.
- [identifier](./vsuseraccount-c.class/identifier.md)
  A string you provide that uniquely identifies the account.
- [requiresSystemTrust](./vsuseraccount-c.class/requiressystemtrust.md)
  A Boolean value that indicates whether the update URL must have a system-trusted certificate.
- [signedOut](./vsuseraccount-c.class/signedout.md)
  A Boolean value that indicates whether the user has signed out of their account.
- [subscriptionBillingCycleEndDate](./vsuseraccount-c.class/subscriptionbillingcycleenddate.md)
  A date that indicates when the billing cycle ends for a paid account.
- [tierIdentifiers](./vsuseraccount-c.class/tieridentifiers.md)
  An array of strings that identify a subset of content from your catalog that the subscriber can play.
- [updateURL](./vsuseraccount-c.class/updateurl.md)
  A URL that points to the application’s JavaScript endpoint for update requests.
### Instance Properties
- [appleSubscription](./vsuseraccount-c.class/applesubscription.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### User account management
- [Signing people in to their media accounts automatically](./signing-people-in-to-media-apps-automatically.md)
  Implement single sign-on for media-streaming apps by managing a sign-in token on a person’s Apple Account.
- [class VSUserAccountManager](./vsuseraccountmanager.md)
  The object that coordinates your app’s user account actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-c.class)*