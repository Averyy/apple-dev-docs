# LowLatencyWriteIsochPipeAsync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Performs an asynchronous write on an isochronous pipe and updates the frame list at primary interrupt time.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*LowLatencyWriteIsochPipeAsync)(void *self, UInt8 pipeRef, void *buf, UInt64 frameStart, UInt32 numFrames, UInt32 updateFrequency, IOUSBLowLatencyIsocFrame *frameList, IOAsyncCallback1 callback, void *refcon);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the interface is not open for exclusive access. Will return kIOUSBLowLatencyBufferNotPreviouslyAllocated or kIOUSBLowLatencyFrameListNotPreviouslyAllocated if the buffer or the frameList were not previously allocated using LowLatencyCreateBuffer().

## Discussion

The LowLatencyReadIsochPipeAsync() and LowLatencyWriteIsochPipeAsync() calls are analogous to ReadIsochPipeAsync() and WriteIsochPipeAsync(). They differ in that the frame list data is updated at *primary interrupt time*. This means that the client can inspect the frStatus and frActCount fields as soon as the transaction completes, without having to wait for the callback to happen (depending on the value of updateFrequency). The callback will still happen when the all the frames have been received.

The client can specify how often the USB stack should update the frame list data by specifying the updateFrequency: this value can range from 0 - 8. If the value is between 1 and 8, the frame list will be updated every updateFrequency milliseconds. If the value is 0, the frame list will only be updated once all the frames in the transfer have been received. For example, consider a transfer with numFrames equal to 64. If the update frequency is 4, the frame list data will be updated every 4 milliseconds. If the update frequency is 0, the frame list will only be updated at the end of the transfer, after the 64 frames have been sent or received. The difference between using an update frequency of 0 and using the non-low latency isoch calls is that in the former case, the frame list will be updated at primary interrupt time, while in the latter, it will be updated at secondary interrupt time. Regardless of the value of updateFrequency, the frame list will *always* be updated on the last frame of a transfer.

The rationale for adding this call is that because completion routines run on the USB Workloop, they can be scheduled to run a number of milliseconds after the USB transfer has finished. This latency is variable and depends on what other higher priority threads are running on the system. This latency presents a problem for applications, such as audio processing, that depend on receiving data, processing it, and sending it back out, and need to do this as fast as possible. Since applications that use isochronous data know when the data should be available, they can look at the frame list at the expected time and note the frActCount and frStatus (and frTimeStamp if needed) and determine how many valid bytes are in their data buffer and whether there was an error. They can then access their data buffer and process the actual data.

In order to update the frame list at primary interrupt time and to allow the client to see that update, the frame list buffer needs to be shared between the kernel and user space. The same thing applies to the data buffer. This is a difference between the low latency isoch calls and the regular isoch calls. The LowLatencyCreateBuffer() call is used to pre-allocate the buffers. The *client* must use that call to allocate the data and the frame list buffers. The client can pass a portion of the buffer that was previously allocated. The USB stack will range-check the data and frame list buffers to make sure they are within the ranges of the buffers previously allocated. This allows the client, if it so desires, to allocate a large data buffer and pass portions of it to the read or write calls. The same applies to the frame list buffers. Of course, the client can also pre-allocate several data buffers and several frame list buffers and use those for each transfer. Once the transfer completes, the buffers can be reused in subsequent calls. When all transfers are finished, the client needs to call LowLatencyDestroyBuffer() for each buffer that was created with LowLatencyCreateBuffer().

The interface must be open for the pipe to exist. The buf pointer and the frameList pointer need to be pre-allocated using LowLatencyCreateBuffer(). After using them, they should be freed using LowLatencyDestroyBuffer().

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `pipeRef`: Index for the desired pipe (1 - GetNumEndpoints).
- `buf`: Buffer to hold the data, previously allocated with LowLatencyCreateBuffer() using a kUSBLowLatencyWriteBuffer type.
- `frameStart`: The bus frame number on which to start the write (obtained from GetBusFrameNumber).
- `numFrames`: The number of frames for which to transfer data.
- `updateFrequency`: Specifies how often, in milliseconds, should the frame list data be updated. Valid range is 0 - 8. If 0, it means that the framelist should be updated at the end of the transfer.
- `frameList`: A pointer to an array of IOUSBLowLatencyIsocFrame structures describing the frames.
- `callback`: An IOAsyncCallback1 method. A message addressed to this callback is posted to the Async port upon completion.
- `refcon`: Arbitrary pointer which is passed as a parameter to the callback routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface192/1559336-lowlatencywriteisochpipeasync)*