# RemoveFromRunLoop

**Framework**: IOKit  
**Kind**: func

Remove the CFRunLoopSource for the notification port from a run loop.

## Declaration

```c
IOReturn ( *RemoveFromRunLoop)(
   IOStreamRef stream,
   CFRunLoopRef runLoop );
```

## Return Value

Returns kIOReturnSuccess if the source was successfully removed from the run loop.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.
- `runLoop`: The run loop from which to remove the notification source.

## See Also

### Run loop operations
- [AddToRunLoop](./api-1809610-addtorunloop.md)
  Add the CFRunLoopSource for the notification port to a run loop.
- [GetRunLoopSource](./api-1809678-getrunloopsource.md)
  Gets a CFRunLoopSource for the CFMachPort used for notifications from the kernel that data is ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1809745-removefromrunloop)*