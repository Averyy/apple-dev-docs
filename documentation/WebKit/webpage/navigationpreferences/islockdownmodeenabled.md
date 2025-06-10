# isLockdownModeEnabled

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether to use Lockdown Mode in the web page.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var isLockdownModeEnabled: Bool { get set }
```

#### Discussion

By default, this reflects whether the user has enabled Lockdown Mode on the device. Update this preference to override the device setting when you implement a per-website or similar setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/islockdownmodeenabled)*