# WritePipeTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Performs an asynchronous write on a **BULK OUT** pipe, with specified timeout values.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*WritePipeTO)(void *self, UInt8 pipeRef, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout);
```

#### Discussion

The interface must be open for the pipe to exist.

If a timeout is specified and the request times out, the driver may need to resynchronize the data toggle. See ClearPipeStall or ClearPipeStallBothEnds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182/1558982-writepipeto)*