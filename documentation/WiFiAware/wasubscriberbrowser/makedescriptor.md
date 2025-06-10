# makeDescriptor()

**Framework**: Wi-Fi Aware  
**Kind**: method

Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func makeDescriptor() -> NWBrowser.Descriptor
```

#### Return Value

A new `Descriptor`  that configures the `NetworkBrowser` for Wi-Fi Aware.

## See Also

- [func configureParameters(NWParameters?) -> NWParameters](wasubscriberbrowser/configureparameters(_:).md)
  Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.
- [func makeEndpoint(from: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?](wasubscriberbrowser/makeendpoint(from:).md)
  Creates a connectable Wi-Fi Aware endpoint from a browse result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/makedescriptor())*