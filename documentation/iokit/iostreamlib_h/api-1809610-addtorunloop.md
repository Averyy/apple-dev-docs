# AddToRunLoop

**Framework**: IOKit  
**Kind**: func

Add the CFRunLoopSource for the notification port to a run loop.

## Declaration

```c
IOReturn ( *AddToRunLoop)(
   IOStreamRef stream,
   CFRunLoopRef runLoop );
```

## Return Value

Returns kIOReturnSuccess if the source was successfully added to the run loop.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.
- `runLoop`: The run loop to which to add the notification source.

## See Also

### Run loop operations
- [GetRunLoopSource](./api-1809678-getrunloopsource.md)
  Gets a CFRunLoopSource for the CFMachPort used for notifications from the kernel that data is ready.
- [RemoveFromRunLoop](./api-1809745-removefromrunloop.md)
  Remove the CFRunLoopSource for the notification port from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1809610-addtorunloop)*