# bitTimeout

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Maximum time a client can delay (by pulling the clock line low) a single bit response.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
AbsoluteTime bitTimeout;
```

## See Also

### Fields
- [byteTimeout](./api-1410362-bytetimeout.md)
  Maximum time a client can delay (by pulling the clock line low) the first bit of a byte response.
- [acknowledgeTimeout](./api-1410369-acknowledgetimeout.md)
  Maximum time to wait for a client to respond with an ACK after writing a byte.
- [startTimeout](./api-1410316-starttimeout.md)
  Maximum time to wait for a client to respond after a start signal.
- [riseFallTime](./api-1410322-risefalltime.md)
  Time to wait after any change in output signal.
- [__reservedA](../ioi2cinterface_h_user-space/ioi2cbustiming/api-1812622-_reserveda.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioi2cbustiming/1410318-bittimeout)*