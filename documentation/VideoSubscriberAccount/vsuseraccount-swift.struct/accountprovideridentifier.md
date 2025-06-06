# accountProviderIdentifier

**Framework**: Videosubscriberaccount  
**Kind**: property

A string that uniquely identifies a provider known to Apple that provides the user account.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+

## Declaration

```swift
var accountProviderIdentifier: String? { get set }
```

#### Discussion

For use only with TV Provider Authentication integrated apps.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-swift.struct/accountprovideridentifier)*