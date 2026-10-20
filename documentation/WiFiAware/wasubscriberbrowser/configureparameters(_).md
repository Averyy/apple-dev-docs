# configureParameters(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Instance Method

Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func configureParameters(_ parameters: NWParameters?) -> NWParameters
```

#### Return Value

A new `NWParameters`, updated to include the Wi-Fi Aware parameters.

## Parameters

- `parameters`: The parameters to use to configure the subscriber.

## See Also

### Creating browser implementation details
- [func makeDescriptor() -> NWBrowser.Descriptor](./makedescriptor%28%29.md)
  Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.
- [func makeEndpoint(from: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?](./makeendpoint%28from%29.md)
  Creates a connectable Wi-Fi Aware endpoint from a browse result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/configureparameters(_:))*