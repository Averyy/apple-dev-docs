# SendInputSyncNotification

**Framework**: IOKit  
**Kind**: func

Notify the kernel side of the stream that input is ready by using a fast trap to call directly into the stream user client driver. This will transfer control to the kernel and continue executing on your same thread, rather than sending the notification to a separate thread.

## Declaration

```c
IOReturn ( *SendInputSyncNotification)(
   IOStreamRef stream,
   UInt32 token );
```

#### Return Value

Returns kIOReturnSuccess if the notification was successfully sent.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.
- `token`: A value to pass to the stream's notification function. This is unused by IOStream but may be used by subclasses.

## See Also

### Notifications
- [SendInputNotification](./api-1810077-sendinputnotification.md)
  Send a notification to the kernel side of the IOStream that data is available in the input queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810090-sendinputsyncnotification)*