# init(_:)

**Framework**: Wi-Fi Aware  
**Kind**: init

Creates a new custom context that provides unique data.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init?(_ data: Data)
```

#### Return Value

A new `Context`, or `nil` if the provided string was too short.

#### Discussion

Custom contexts may use any data. Set the same byte value on the local and remote devices in order to generate the same shared secret.

## Parameters

- `data`: The data to use as the underlying context, which must be greater than or equal to   bytes long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/context/init(_:)-74fai)*