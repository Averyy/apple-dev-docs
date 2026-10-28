# vendorName

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Role**: Instance Property

The human-readable name of the manufacturer or vendor of the physical device as a person would understand it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
let vendorName: String
```

## Discussion

The system receives this data from the device within an DNS-SD TXT record. The value set in the `vendorName` property is the  value that follows the DNS-SD TXT record key:

```
vendorName=
```

The system interprets the value as an <= 63-byte UTF-8 string and may truncate it if it’s longer than 63 bytes. Refer to [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763#section-6.3) for more information on the over-the-air encoding.

## See Also

### Receiving device information
- [let modelName: String](./modelname.md)
  The human-readable model name of the physical device as a person can understand it.
- [let pairingName: String](./pairingname.md)
  The human-readable name of the physical device as a person sees it during initial pairing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/pairinginfo-swift.struct/vendorname)*