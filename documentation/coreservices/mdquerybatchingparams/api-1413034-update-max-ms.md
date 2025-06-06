# update_max_ms

**Framework**: Core Services  
**Kind**: structp

The maximum number of milliseconds that can passbefore an update notification is sent. This value is advisory, inthat the notification will be triggered at some point after `update_max_ms` millisecondshave passed since the query began accumulating results. This valueis used only during the live-update phase of a query.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
var update_max_ms: Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdquerybatchingparams/1413034-update_max_ms)*