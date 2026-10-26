# VisionEntitlementServices

**Framework**: VisionEntitlementServices  
**Kind**: module  
**Role**: Framework

Inspect an app’s visionOS Enterprise license state and its approved managed entitlements.

**Availability**:
- visionOS 26.0+

#### Overview

Enterprise apps on visionOS unlock managed entitlements through a signed license installed on the device. This includes main camera access, barcode detection, or the elevated App Compute Category. Use VisionEntitlementServices to read the current license state at runtime and to check which managed entitlements the license approves for the calling app.

Access to the license state is read-only. Use [`shared`](./enterpriselicensedetails/shared.md) to obtain the singleton for the current process, and use [`shared`](./appcomputecategory/shared.md) to observe the elevated App Compute Category.

## Topics

### Reading license state
- [class EnterpriseLicenseDetails](./enterpriselicensedetails.md)
  Class to retrieve and inspect information relating to visionOS Enterprise License and Managed Entitlement status and validity.
- [EnterpriseLicenseDetails.EnterpriseEntitlement](./enterpriselicensedetails/enterpriseentitlement.md)
- [EnterpriseLicenseDetails.Status](./enterpriselicensedetails/status.md)
### App Compute Category
- [class AppComputeCategory](./appcomputecategory.md)
  Functionality to track App Compute Category settings and whether the system has completed the enabling of additional configurations which are triggered by having a properly licensed app open which includes the AppComputeCategory Enterprise entitlement
- [AppComputeCategory.Status](./appcomputecategory/status-swift.enum.md)
### Variables
- [VisionEntitlementServicesVersionNumber](./visionentitlementservicesversionnumber.md)
  Project version number for VisionEntitlementServices.
- [VisionEntitlementServicesVersionString](./visionentitlementservicesversionstring.md)
  Project version string for VisionEntitlementServices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionentitlementservices)*