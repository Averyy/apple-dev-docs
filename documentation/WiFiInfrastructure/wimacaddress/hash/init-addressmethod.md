# init(address:method:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates a new `Hash` from the given MAC Address, using a randomly-generated salt.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init?(address: WIMACAddress, method: WIMACAddress.Hash.Method = .sha256)
```

## Parameters

- `address`: The MAC Address to hash.
- `method`: The method to use to generate the hash. Defaults to `.sha256`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/hash/init(address:method:))*