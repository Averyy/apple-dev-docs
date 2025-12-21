# configureParameters(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func configureParameters(_ parameters: NWParameters?) -> NWParameters
```

#### Return Value

A new `NWParameters`, updated to include the Wi-Fi Aware parameters.

## Parameters

- `parameters`: The parameters to use to configure the subscriber.

## See Also

- [func makeDescriptor() -> NWBrowser.Descriptor](wasubscriberbrowser/makedescriptor.md)
  Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.
- [func makeEndpoint(from: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?](wasubscriberbrowser/makeendpoint(from:).md)
  Creates a connectable Wi-Fi Aware endpoint from a browse result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/configureparameters(_:))*