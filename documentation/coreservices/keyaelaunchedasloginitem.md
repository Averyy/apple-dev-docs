# keyAELaunchedAsLogInItem

**Framework**: Core Services  
**Kind**: data

If present in a `kAEOpenApplication` event, the receiving application was launched as a login item and should only perform actions suitable to that environment—for example, it probably shouldn't open an untitled document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var keyAELaunchedAsLogInItem: AEKeyword { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/keyaelaunchedasloginitem)*