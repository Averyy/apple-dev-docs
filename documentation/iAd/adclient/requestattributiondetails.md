# requestAttributionDetails(_:)

**Framework**: iAd  
**Kind**: method

Gets an attribution response.

## Declaration

```swift
func requestAttributionDetails() async throws -> [String : NSObject]
```

## Mentions

- [Setting Up Apple Search Ads Attribution](setting-up-apple-search-ads-attribution.md)
- [iAd Changelog](iad-changelog.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestAttributionDetails() async throws -> [String : NSObject]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

For iOS 14 and later, obtaining an attribution response depends on the calling app’s [`trackingAuthorizationStatus`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/trackingAuthorizationStatus) value and the device-level setting Allow Apps to Request to Track (AAtRtT). The AAtRtT setting allows users to opt in or out of allowing apps to request user consent to access app-related data that third parties can use for both attribution and tracking the user or the device. The following table shows the combination of tracking interactions and expected attribution payload response.

|  |  |  |
| --- | --- | --- |
| On | Attribution Response - See [`Retrieve the Attribution Dictionary`](setting-up-apple-search-ads-attribution#Retrieve-the-Attribution-Dictionary.md) | [`ATTrackingManager.AuthorizationStatus.authorized`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/authorized) |
| Off | Attribution Response - See [`Retrieve the Attribution Dictionary`](setting-up-apple-search-ads-attribution#Retrieve-the-Attribution-Dictionary.md) | [`ATTrackingManager.AuthorizationStatus.authorized`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/authorized) |
| On | [`trackingRestrictedOrDenied`](adclienterror-swift.struct/trackingrestrictedordenied.md) | [`ATTrackingManager.AuthorizationStatus.notDetermined`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/notDetermined) |
| Off | [`trackingRestrictedOrDenied`](adclienterror-swift.struct/trackingrestrictedordenied.md) | [`ATTrackingManager.AuthorizationStatus.notDetermined`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/notDetermined) |
| On | [`trackingRestrictedOrDenied`](adclienterror-swift.struct/trackingrestrictedordenied.md) | [`ATTrackingManager.AuthorizationStatus.denied`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/denied) |
| Off | [`trackingRestrictedOrDenied`](adclienterror-swift.struct/trackingrestrictedordenied.md) | [`ATTrackingManager.AuthorizationStatus.denied`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/denied) |
| Off - the user can’t change the setting. | [`trackingRestrictedOrDenied`](adclienterror-swift.struct/trackingrestrictedordenied.md) | [`ATTrackingManager.AuthorizationStatus.restricted`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/restricted) |


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclient/requestattributiondetails(_:))*