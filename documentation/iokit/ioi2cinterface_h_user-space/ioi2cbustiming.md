# IOI2CBusTiming

**Framework**: IOKit  
**Kind**: tag

A structure defining low level timing for an I2C bus.

## Declaration

```c
struct IOI2CBusTiming {
   AbsoluteTime bitTimeout;
   AbsoluteTime byteTimeout;
   AbsoluteTime acknowledgeTimeout;
   AbsoluteTime startTimeout;
   AbsoluteTime holdTime;
   AbsoluteTime riseFallTime;
   UInt32 __reservedA[8];
};
```

## Overview

This structure is used to specify timeouts and pulse widths for an I2C bus implementation.

## Topics

### Fields
- [bitTimeout](../ioi2cbustiming/api-1410318-bittimeout.md)
  Maximum time a client can delay (by pulling the clock line low) a single bit response.
- [byteTimeout](../ioi2cbustiming/api-1410362-bytetimeout.md)
  Maximum time a client can delay (by pulling the clock line low) the first bit of a byte response.
- [acknowledgeTimeout](../ioi2cbustiming/api-1410369-acknowledgetimeout.md)
  Maximum time to wait for a client to respond with an ACK after writing a byte.
- [startTimeout](../ioi2cbustiming/api-1410316-starttimeout.md)
  Maximum time to wait for a client to respond after a start signal.
- [riseFallTime](../ioi2cbustiming/api-1410322-risefalltime.md)
  Time to wait after any change in output signal.
- [__reservedA](./ioi2cbustiming/api-1812622-_reserveda.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioi2cinterface_h_user-space/ioi2cbustiming)*