# ReadPipeTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Performs a read on a **BULK IN** pipe, specifying timeout values.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ReadPipeTO)(void *self, UInt8 pipeRef, void *buf, UInt32 *size, UInt32 noDataTimeout, UInt32 completionTimeout);
```

## Discussion

The interface must be open for the pipe to exist.

If a timeout is specified and the request times out, the driver may need to resynchronize the data toggle. See ClearPipeStall or ClearPipeStallBothEnds.

Timeouts do not apply to interrupt pipes, so you should use the ReadPipe API to perform a read from an interrupt pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182/1559627-readpipeto)*