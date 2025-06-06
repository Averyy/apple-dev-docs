# progress_max_ms

**Framework**: Core Services  
**Kind**: structp

The maximum number of milliseconds that can passbefore additional progress notifications are sent. This value isadvisory, in that the notification will be triggered at some pointafter `progress_max_ms` millisecondshave passed since the query began accumulating results. This valueis used only during the initial result-gathering phase of a query.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
var progress_max_ms: Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdquerybatchingparams/1413043-progress_max_ms)*