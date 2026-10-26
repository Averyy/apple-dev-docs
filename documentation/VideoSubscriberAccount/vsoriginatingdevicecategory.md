# VSOriginatingDeviceCategory

**Framework**: Video Subscriber Account  
**Kind**: enum  
**Role**: Enumeration

Constants that represent whether the device from which the user originally registered is mobile.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```c
enum VSOriginatingDeviceCategory : NSInteger;
```

## Topics

### Originating device categories
- [VSOriginatingDeviceCategoryMobile](./vsoriginatingdevicecategory/vsoriginatingdevicecategorymobile.md)
  A constant that indicates the original registering device is mobile.
- [VSOriginatingDeviceCategoryOther](./vsoriginatingdevicecategory/vsoriginatingdevicecategoryother.md)
  A constant that indicates the original registering device is not mobile.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsoriginatingdevicecategory)*