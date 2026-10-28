# ReadPipeAsyncTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Performs an asynchronous read on a **BULK IN** pipe, with specified timeout values.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ReadPipeAsyncTO)(void *self, UInt8 pipeRef, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout, IOAsyncCallback1 callback, void *refcon);
```

## Discussion

The interface must be open for the pipe to exist.

If a timeout is specified and the request times out, the driver may need to resynchronize the data toggle. See ClearPipeStall or ClearPipeStallBothEnds.

Timeouts do not apply to interrupt pipes, so you should use the ReadPipeAsync API to perform an asynchronous read from an interrupt pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182/1559295-readpipeasyncto)*