# status

**Framework**: VisionEntitlementServices  
**Kind**: property

Informs calling app whether or not the system has finished enabling the settings that are enabled by the App Compute Category Enterprise entitlement and if they are currently in force.  If they have been, it will return `.high`, otherwise it will return `.normal` If the app does not have the appropriate license to fetch this information it will return `.notAuthorized`

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var status: AppComputeCategory.Status { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory/status-swift.property)*