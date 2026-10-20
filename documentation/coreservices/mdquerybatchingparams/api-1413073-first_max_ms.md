# first_max_ms

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

The maximum number of milliseconds that can passbefore the first progress notification is sent. This value is advisory,in that the notification will be triggered at some point after `first_max_ms` millisecondshave passed since the query began accumulating results. This valueis used only during the initial result-gathering phase of a query.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
var first_max_ms: Int
```

```c
size_t first_max_ms;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdquerybatchingparams/1413073-first_max_ms)*