# setLogoutCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the callback to be called when a logout attempt is complete.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setLogoutCallback)(void *self, void *refCon, IOFWSBP2LogoutCallback callback);
```

#### Discussion

The supplied callback is called when a logout attempt has completed. "status" in the callback's params should be checked to determine the success or failure of the logout attempt. The "refCon" field in the params will return the refcon set with setRefCon. If "statusBlock" is non-null then logout status was written and it has been supplied here. Note: all buffers supplied to callbacks are only valid for the duration of the callback. Also, you are not to modify the contents of any supplied buffer.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `refCon`: refCon passed to callback.
- `callback`: address of callback method of type FWSBP2LogoutCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590492-setlogoutcallback)*