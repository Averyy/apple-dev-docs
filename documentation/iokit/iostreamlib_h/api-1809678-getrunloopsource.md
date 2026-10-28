# GetRunLoopSource

**Framework**: IOKit  
**Kind**: func

Gets a CFRunLoopSource for the CFMachPort used for notifications from the kernel that data is ready.

## Declaration

```c
CFRunLoopSourceRef ( *GetRunLoopSource)(
   IOStreamRef stream );
```

## Return Value

The CFRunLoopSourceRef for the run loop source, or NULL if there was an error creating the source.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.

## See Also

### Run loop operations
- [AddToRunLoop](./api-1809610-addtorunloop.md)
  Add the CFRunLoopSource for the notification port to a run loop.
- [RemoveFromRunLoop](./api-1809745-removefromrunloop.md)
  Remove the CFRunLoopSource for the notification port from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1809678-getrunloopsource)*