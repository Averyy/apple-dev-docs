# makeDescriptor()

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Instance Method

Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func makeDescriptor() -> NWBrowser.Descriptor
```

#### Return Value

A new `Descriptor`  that configures the `NetworkBrowser` for Wi-Fi Aware.

## See Also

### Creating browser implementation details
- [func configureParameters(NWParameters?) -> NWParameters](./configureparameters%28_%29.md)
  Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.
- [func makeEndpoint(from: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?](./makeendpoint%28from%29.md)
  Creates a connectable Wi-Fi Aware endpoint from a browse result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/makedescriptor())*