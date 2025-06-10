# pairingInfo

**Framework**: Wi-Fi Aware  
**Kind**: property

The unauthenticated information provided by the device before a person pairs it for the first time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
let pairingInfo: WAPairedDevice.PairingInfo?
```

#### Discussion

The value is `nil` if the information is unavailable. The values provide a capture of what the system receives prior to the first pairing the device, and don’t reflect any information received post-pairing. If your app needs more up-to-date info, query the device via the secure Wi-Fi Aware data path.

> ⚠️ **Warning**:  Don’t use these values for any purpose other than to assist a person during the initial one-time pairing process. Because the system receives the values before the initial pairing, they’re transmitted over an insecure, unauthenticated, and unencrypted channel. Consequently, they may be intercepted or manipulated by an attacker, making it impossible to verify their accuracy. Therefore, if your app requires reliable and detailed information about the connected device, it needs to obtain it through the secure Wi-Fi Aware data path after pairing is complete, rather than relying on the content in this structure.

## See Also

- [WAPairedDevice.PairingInfo](wapaireddevice/pairinginfo-swift.struct.md)
  A collection of unauthenticated information the system receives from a device before it’s paired for the first time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/pairinginfo-swift.property)*