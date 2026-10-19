# AppComputeCategory

**Framework**: VisionEntitlementServices  
**Kind**: class

Functionality to track App Compute Category settings and whether the system has completed the enabling of additional configurations which are triggered by having a properly licensed app open which includes the AppComputeCategory Enterprise entitlement

**Availability**:
- visionOS 26.0+

## Declaration

```swift
class AppComputeCategory
```

## Topics

### Instance Properties
- [var status: AppComputeCategory.Status](appcomputecategory/status-swift.property.md)
  Informs calling app whether or not the system has finished enabling the settings that are enabled by the App Compute Category Enterprise entitlement and if they are currently in force.  If they have been, it will return `.high`, otherwise it will return `.normal` If the app does not have the appropriate license to fetch this information it will return `.notAuthorized`
### Type Properties
- [static let shared: AppComputeCategory](appcomputecategory/shared.md)
### Enumerations
- [AppComputeCategory.Status](appcomputecategory/status-swift.enum.md)

## See Also

- [AppComputeCategory.Status](appcomputecategory/status-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory)*