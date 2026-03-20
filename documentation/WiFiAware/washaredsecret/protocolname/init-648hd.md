# init(_:)

**Framework**: Wi-Fi Aware  
**Kind**: init

Creates a custom protocol with the provided unique string.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init?(_ data: Data)
```

#### Return Value

A new [`WASharedSecret.ProtocolName`](washaredsecret/protocolname.md), or `nil` if the provided data was too short.

#### Discussion

Custom protocols need to specify data that identifies the protocol that will use the shared secret. Set the same value on the local and remote devices in order to generate the same shared secret.

## Parameters

- `data`: The data to use as the underlying protocol name, which must be greater than or equal to 3 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/protocolname/init(_:)-648hd)*