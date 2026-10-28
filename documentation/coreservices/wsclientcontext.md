# WSClientContext

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

An optional context that can contain data you want passed to your callback.

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef struct WSClientContext {
    ...
} WSClientContext;
```

## Overview

Several calls in the Web Services Core framework take a callback with an optional context pointer.  The context is copied and the info pointer retained.  When the callback is made, the info pointer is passed to the callback.

## Topics

### Instance Properties
- [copyDescription](./wsclientcontext/api-1508458-copydescription.md)
  Callback made on the info pointer. This field may be NULL.
- [info](./wsclientcontext/api-1508462-info.md)
  A pointer to your information to be passed to your callback.
- [release](./wsclientcontext/api-1508435-release.md)
  Callback made on the info pointer. This field may be NULL.
- [retain](./wsclientcontext/api-1508453-retain.md)
  Callback made on the info pointer. This field may be NULL.
- [version](./wsclientcontext/api-1508448-version.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsclientcontext)*