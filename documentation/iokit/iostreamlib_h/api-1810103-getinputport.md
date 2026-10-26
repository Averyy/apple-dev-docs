# GetInputPort

**Framework**: IOKit  
**Kind**: func

Get the notification port for buffers moving in from user to kernel space.

## Declaration

```c
CFMachPortRef ( *GetInputPort)(
   IOStreamRef stream );
```

#### Return Value

A CFMachPortRef for the input notification port.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.

## See Also

### Input and output
- [GetInputQueue](./api-1810117-getinputqueue.md)
  Get the shared memory queue for buffers moving in from user to kernel space.
- [GetOutputPort](./api-1810125-getoutputport.md)
  Get the notification port for buffers moving out from kernel to user space.
- [GetOutputQueue](./api-1810141-getoutputqueue.md)
  Get the shared memory queue for buffers moving out from kernel to user space.
- [SetOutputCallback](./api-1810149-setoutputcallback.md)
  Set the callback function to be called when a new buffer is available from the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810103-getinputport)*