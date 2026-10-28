# GetInputQueue

**Framework**: IOKit  
**Kind**: func

Get the shared memory queue for buffers moving in from user to kernel space.

## Declaration

```c
IOStreamBufferQueue *( *GetInputQueue)(
   IOStreamRef stream );
```

## Return Value

A pointer to the shared memory IOStreamBufferQueue structure for the input queue.

## Overview

If you use the notification functions, you should never need to access the queues directly.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.

## See Also

### Input and output
- [GetInputPort](./api-1810103-getinputport.md)
  Get the notification port for buffers moving in from user to kernel space.
- [GetOutputPort](./api-1810125-getoutputport.md)
  Get the notification port for buffers moving out from kernel to user space.
- [GetOutputQueue](./api-1810141-getoutputqueue.md)
  Get the shared memory queue for buffers moving out from kernel to user space.
- [SetOutputCallback](./api-1810149-setoutputcallback.md)
  Set the callback function to be called when a new buffer is available from the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810117-getinputqueue)*