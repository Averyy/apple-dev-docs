# tlsPSK

**Framework**: Wi-Fi Aware  
**Kind**: property

Derive a shared secret to bootstrap TLS, using the resulting shared secret as a TLS Pre-Shared Key.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
static let tlsPSK: WASharedSecret.ProtocolName
```

#### Discussion

Best practices for TLS security are described in [`NIST Special Publication 800-52`](https://developer.apple.comhttps://csrc.nist.gov/pubs/sp/800/52/r2/final). TLS 1.3 is recommended.

Specifying this value will use the “`TLS-PSK`” string as the protocol name when deriving the shared secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/protocolname/tlspsk)*