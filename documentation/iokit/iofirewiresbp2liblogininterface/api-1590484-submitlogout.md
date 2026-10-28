# submitLogout

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Attempts to logout of the LUN.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*submitLogout)(void *self);
```

## Return Value

Returns kIOReturnSuccess if logout has successfully begun.

## Discussion

This call begins the logout process. If kIOReturnSuccess is returned from this call then the logoutCompletion routine will be called when the logout completes (successfully or unsuccesfully).

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590484-submitlogout)*