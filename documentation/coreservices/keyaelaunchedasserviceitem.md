# keyAELaunchedAsServiceItem

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var keyAELaunchedAsServiceItem: AEKeyword { get }
```

#### Discussion

If present in a `kAEOpenApplication` event, the receiving application was launched as a service item and should only perform actions suitable to that environment—for example, it probably shouldn't open an untitled document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/keyaelaunchedasserviceitem)*