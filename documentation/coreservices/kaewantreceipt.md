# kAEWantReceipt

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAEWantReceipt: Int { get }
```

#### Discussion

Deprecated and unsupported in macOS. The return receipt preference—the sender wants to receive a return receipt for this Apple event from the Event Manager. (A return receipt means only that the receiving application accepted the Apple event the Apple event may or may not be handled successfully after it is accepted.) If the receiving application does not send a return receipt before the request times out, `AESend` returns `errAETimeout` as its function result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaewantreceipt)*