# EnterpriseLicenseDetails

**Framework**: VisionEntitlementServices  
**Kind**: class  
**Role**: Class

Class to retrieve and inspect information relating to visionOS Enterprise License and Managed Entitlement status and validity.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
class EnterpriseLicenseDetails
```

## Topics

### Instance Properties
- [var approvedEntitlements: [EnterpriseLicenseDetails.EnterpriseEntitlement]](./enterpriselicensedetails/approvedentitlements.md)
- [var expirationTimestamp: Date](./enterpriselicensedetails/expirationtimestamp.md)
- [var licenseStatus: EnterpriseLicenseDetails.Status](./enterpriselicensedetails/licensestatus.md)
### Instance Methods
- [func isApproved(for: EnterpriseLicenseDetails.EnterpriseEntitlement) -> Bool](./enterpriselicensedetails/isapproved%28for%29.md)
  Returns whether the app is licensed to use the provided `EnterpriseEntitlement` and was built with that `EnterpriseEntitlement`
### Type Properties
- [static let shared: EnterpriseLicenseDetails](./enterpriselicensedetails/shared.md)
### Enumerations
- [EnterpriseLicenseDetails.EnterpriseEntitlement](./enterpriselicensedetails/enterpriseentitlement.md)
- [EnterpriseLicenseDetails.Status](./enterpriselicensedetails/status.md)

## See Also

### Reading license state
- [EnterpriseLicenseDetails.EnterpriseEntitlement](./enterpriselicensedetails/enterpriseentitlement.md)
- [EnterpriseLicenseDetails.Status](./enterpriselicensedetails/status.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails)*