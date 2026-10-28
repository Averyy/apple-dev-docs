# fromCurrentDevice

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user originated their account on the current device.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly, getter=isFromCurrentDevice) BOOL fromCurrentDevice;
```

## Discussion

Accounts that you fetch using [`VSUserAccountManager`](../vsuseraccountmanager.md) may be from other devices signed into the same iCloud account.

## See Also

### User account information
- [accountProviderIdentifier](./accountprovideridentifier.md)
  A string that uniquely identifies a TV provider known to Apple that provides the user account.
- [accountType](./accounttype.md)
  A constant that represents whether a user has access to paid content.
- [authenticationData](./authenticationdata.md)
  A string that represents an authentication token for the user account to authenticate with the TV provider.
- [billingIdentifier](./billingidentifier.md)
  A string that Identifies the billing group associated with the user account’s subscription.
- [deviceCategory](./devicecategory.md)
  A constant that indicates whether the device from which the user registered is mobile.
- [VSOriginatingDeviceCategory](../vsoriginatingdevicecategory.md)
  Constants that represent whether the device from which the user originally registered is mobile.
- [identifier](./identifier.md)
  A string you provide that uniquely identifies the account.
- [requiresSystemTrust](./requiressystemtrust.md)
  A Boolean value that indicates whether the update URL must have a system-trusted certificate.
- [signedOut](./signedout.md)
  A Boolean value that indicates whether the user has signed out of their account.
- [subscriptionBillingCycleEndDate](./subscriptionbillingcycleenddate.md)
  A date that indicates when the billing cycle ends for a paid account.
- [tierIdentifiers](./tieridentifiers.md)
  An array of strings that identify a subset of content from your catalog that the subscriber can play.
- [updateURL](./updateurl.md)
  A URL that points to the application’s JavaScript endpoint for update requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-c.class/fromcurrentdevice)*