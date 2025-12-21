# isLockdownModeEnabled

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether to use Lockdown Mode in the web page.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isLockdownModeEnabled: Bool { get set }
```

#### Discussion

By default, this reflects whether the user has enabled Lockdown Mode on the device. Update this preference to override the device setting when you implement a per-website or similar setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/islockdownmodeenabled)*