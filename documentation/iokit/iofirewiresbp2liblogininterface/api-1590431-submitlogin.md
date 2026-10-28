# submitLogin

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Attempts to login to the LUN.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*submitLogin)(void *self);
```

## Return Value

Returns kIOReturnSuccess login has successlly begun.

## Discussion

This call begins the login process. The login object should be configured prior to this call. If kIOReturnSuccess is returned from this call then the loginCompletion routine will be called when the login completes (successfully or unsuccesfully).

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590431-submitlogin)*