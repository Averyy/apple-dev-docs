# makeEndpoint(from:)

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Instance Method

Creates a connectable Wi-Fi Aware endpoint from a browse result.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func makeEndpoint(from browseResult: NWBrowser.Result) throws -> WASubscriberBrowser.Endpoint?
```

## Return Value

A `WAEndpoint` that you can connect to, or `nil` if it can’t be created.

## Discussion

> **Throws**: An error if the result isn’t valid.

## Parameters

- `browseResult`: The result of the `NWBrowser` operation.

## See Also

### Creating browser implementation details
- [func makeDescriptor() -> NWBrowser.Descriptor](./makedescriptor%28%29.md)
  Makes a descriptor that can create a network browser for a Wi-Fi Aware subscribe operation.
- [func configureParameters(NWParameters?) -> NWParameters](./configureparameters%28_%29.md)
  Returns the parameters to use to configure the Wi-Fi Aware subscriber and the subsequent connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/makeendpoint(from:))*