# ipsecPSK

**Framework**: Wi-Fi Aware  
**Kind**: property

Derive a shared secret to bootstrap IPSec, using the resulting shared secret as the IPSec Pre-Shared Key.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static let ipsecPSK: WASharedSecret.ProtocolName
```

#### Discussion

Best practices for IPSec security are described in [`NIST Special Publication 800-77`](https://developer.apple.comhttps://csrc.nist.gov/pubs/sp/800/77/r1/final). IKEv2 and IPSec-v3 are recommended.

Specifying this value will use the “`IPSec-PSK`” string as the protocol name when deriving the shared secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/protocolname/ipsecpsk)*