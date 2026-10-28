# setLoginFlags

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets login configuration flags.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setLoginFlags)(void *self, UInt32 flags);
```

## Discussion

Configures the login behavior according to the provided flags. Currently two flags are defined for this API. kFWSBP2ExclusiveLogin sets the exclusive login bit in the login ORB. kFWSBP2DontSynchronizeMgmtAgent allows simultaneous logins or reconnects to LUNs with a common management agent (ie LUNs in the same unit directory).

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `flags`: the login configuration flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590531-setloginflags)*