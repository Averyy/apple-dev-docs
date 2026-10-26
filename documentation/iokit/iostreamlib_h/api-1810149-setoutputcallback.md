# SetOutputCallback

**Framework**: IOKit  
**Kind**: func

Set the callback function to be called when a new buffer is available from the kernel.

## Declaration

```c
IOReturn ( *SetOutputCallback)(
   IOStreamRef stream,
   IOStreamOutputCallback callback,
   void *context );
```

#### Return Value

Returns kIOReturnSuccess if the callback was successfully set or removed.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on. Pass NULL to remove the callback.

## See Also

### Input and output
- [GetInputPort](./api-1810103-getinputport.md)
  Get the notification port for buffers moving in from user to kernel space.
- [GetInputQueue](./api-1810117-getinputqueue.md)
  Get the shared memory queue for buffers moving in from user to kernel space.
- [GetOutputPort](./api-1810125-getoutputport.md)
  Get the notification port for buffers moving out from kernel to user space.
- [GetOutputQueue](./api-1810141-getoutputqueue.md)
  Get the shared memory queue for buffers moving out from kernel to user space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810149-setoutputcallback)*