# makeEndpoint(from:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Creates a connectable Wi-Fi Aware endpoint from a browse result.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func makeEndpoint(from browseResult: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?
```

#### Return Value

A `WAEndpoint` that you can connect to, or `nil` if it can’t be created.

#### Discussion

> **Note**:  An error if the result isn’t valid.

## Parameters

- `browseResult`: The result of the   operation.

## See Also

- [func makeDescriptor() -> NWBrowser.Descriptor](wasubscriberbrowser/makedescriptor.md)
  Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.
- [func configureParameters(NWParameters?) -> NWParameters](wasubscriberbrowser/configureparameters(_:).md)
  Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/makeendpoint(from:))*