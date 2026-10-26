# setUnsolicitedStatusNotify

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the callback to be called on normal command status.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setUnsolicitedStatusNotify)(void *self, void *refCon, IOFWSBP2NotifyCallback callback);
```

#### Discussion

The supplied callback is called when unsolicited status is recieved. "notificationEvent" in the callback's params will indicate what happened. In this case it will be set to kFWSBP2UnsolicitedStatus. If "len" is non-zero then "message" contains the data written to the status block. Note: any buffers returned by callbacks are only valid for the duration of the login and should not have their contents modified. The "refCon" field in the callback's params will return the refcon set with setRefCon.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `refCon`: refCon passed to callback.
- `callback`: address of callback method of type FWSBP2NotifyCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590568-setunsolicitedstatusnotify)*