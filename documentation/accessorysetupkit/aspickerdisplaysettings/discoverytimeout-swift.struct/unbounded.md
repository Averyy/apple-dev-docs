# unbounded

**Framework**: AccessorySetupKit  
**Kind**: property

A picker discovery that only times out when the app tells it to.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+

## Declaration

```swift
static let unbounded: ASPickerDisplaySettings.DiscoveryTimeout
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

Use this timeout value if you set the picker display option [`filterDiscoveryResults`](aspickerdisplaysettings/options-swift.struct/filterdiscoveryresults.md) and need unlimited time for filtering. After performing manual discovery, perform the manual timeout by calling the [`ASAccessorySession`](asaccessorysession.md) method [`finishPickerDiscovery(completionHandler:)`](asaccessorysession/finishpickerdiscovery(completionhandler:).md). This process shows a timeout message if your filtering added no accessories to the picker, or returns silently if you updated the picker.

## See Also

- [class var `default`: ASPickerDisplaySettings](aspickerdisplaysettings/default.md)
  An empty settings object.
- [static let short: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/short.md)
  A picker discovery timeout value that times out after about about 60 seconds.
- [static let medium: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/medium.md)
  A picker discovery timeout value that times out after about two minutes.
- [static let long: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/long.md)
  A picker discovery timeout value that times out after about five minutes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings/discoverytimeout-swift.struct/unbounded)*