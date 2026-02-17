# init(_:)

**Framework**: Wi-Fi Aware  
**Kind**: init

Creates a new custom context that provides a unique string.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init?(_ string: String)
```

#### Return Value

A new `Context`, or `nil` if the provided string was too short

#### Discussion

The custom context may use any string that is representable as UTF-8, and which normalizes to the same value when represented as bytes. A best practice is to use ASCII-compatible values to avoid normalization issues. Set the same byte value on the local and remote devices in order to generate the same shared secret.

## Parameters

- `string`: The string to use as the underlying context, which must be equal to or greater than three characters long. The framework converts the string to UTF-8 prior to hashing it in the derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/context/init(_:)-8fpqd)*