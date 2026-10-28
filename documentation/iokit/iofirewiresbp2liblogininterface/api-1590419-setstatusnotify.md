# setStatusNotify

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the callback to be called on normal command status.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setStatusNotify)(void *self, void *refCon, IOFWSBP2NotifyCallback callback);
```

## Discussion

The supplied callback is called when normal command status is recieved, when a normal command times out, or when a normal command is aborted. "notificationEvent" in the callback's params will indicate what happened. It will be set to one of the following values: kFWSBP2NormalCommandReset, kFWSBP2NormalCommandStatus, or kFWSBP2NormalCommandTimeout. If the event type is kFWSBP2NormalCommandTimeout and "len" is non-zero then "message" contains the data written to the status block.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `refCon`: refCon passed to callback.
- `callback`: Address of callback method of type FWSBP2NotifyCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590419-setstatusnotify)*