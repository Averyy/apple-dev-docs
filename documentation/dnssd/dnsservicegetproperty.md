# DNSServiceGetProperty(_:_:_:)

**Framework**: dnssd  
**Kind**: func

Gets the specified property of a service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func DNSServiceGetProperty(_ property: UnsafePointer<CChar>!, _ result: UnsafeMutableRawPointer!, _ size: UnsafeMutablePointer<UInt32>!) -> DNSServiceErrorType
```

## Mentions

- [_DNS_SD_H](dns_sd_h.md)

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success, or kDNSServiceErr_ServiceNotRunning if the daemon (or “system service” on Windows) is not running.

## Parameters

- `property`: The requested property. Currently the only property defined is  .
- `result`: Place to store result. For retrieving DaemonVersion, this should be the address of a uint32_t.
- `size`: Pointer to uint32_t containing size of the result location. For retrieving DaemonVersion, this should be sizeof(uint32_t). On return the uint32_t is updated to the size of the data returned. For DaemonVersion, the returned size is always sizeof(uint32_t), but future properties could be defined which return variable-sized results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicegetproperty(_:_:_:))*