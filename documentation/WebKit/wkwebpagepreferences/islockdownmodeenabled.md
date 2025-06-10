# isLockdownModeEnabled

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether to use Lockdown Mode in the web view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isLockdownModeEnabled: Bool { get set }
```

#### Discussion

By default, this reflects whether the user has enabled Lockdown Mode on the device. Update this preference to override the device setting when you implement a per-website or similar setting.

For more information about Lockdown Mode, see [`About Lockdown Mode`](https://developer.apple.comhttps://support.apple.com/en-us/HT212650).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/islockdownmodeenabled)*