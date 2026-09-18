# IOUserVideoStream

**Framework**: VideoDriverKit  
**Kind**: class

A video stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoStream;
```

#### Overview

[`IOUserVideoDevice`](iouservideodevice.md) instances own [`IOUserVideoStream`](iouservideostream.md) instances. [`IOUserVideoStream`](iouservideostream.md) allocates memory descriptors that the host uses for running IO. Changes to the owning [`IOUserVideoDevice`](iouservideodevice.md) will potentially update formats on the underlying [`IOUserVideoStream`](iouservideostream.md).

## Topics

### Creating a video stream
- [Create](iouservideostream/create.md)
- [init](iouservideostream/init.md)
  Initializes an video stream.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
### Freeing a video stream
- [free](iouservideostream/free.md)
  Frees the video stream.
### Getting information about the class
- [GetClassID](iouservideostream/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideostream/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Performing I/O
- [StartIO](iouservideostream/startio.md)
  Tells the stream to start IO.
- [StopIO](iouservideostream/stopio.md)
  Tells the stream to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [InputNotification](iouservideostream/inputnotification.md)
### Working with stream formats
- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
  Sets the current stream format.
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
  Gets the current basic description of the stream.
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
  Sets the available descriptions for the stream.
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
  Gets the available basic descriptions for the stream.
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
  Gets the number of available description for the stream.
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
  Gets the direction of the stream.
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
  The direction of a video stream.
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
  Sets whether that the stream is active and doing IO.
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)
  Gets the stream activity state.
### Working with stream terminals
- [SetTerminalType](iouservideostream/setterminaltype.md)
  Sets the terminal type of the stream.
- [GetTerminalType](iouservideostream/getterminaltype.md)
  Gets the terminal type of the stream.
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)
  The terminal type of video stream.
### Working with memory descriptors
- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
  Gets the memory descriptor used for the control data part of a buffer.
- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
  Gets the memory descriptor used for the video data part of a buffer.
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
  Returns an memory descriptorrepesenting the shared memory output queue buffer.
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)
  Returns an memory descriptor for the shared memory input queue buffer.
- [GetMemoryObjectID](iouservideostream/getmemoryobjectid.md)
  Gets the video object identifier for a memory object.
### Managing stream changes
- [HandleChangeCurrentStreamFormat](iouservideostream/handlechangecurrentstreamformat.md)
  The system calls this virtual method when the stream’s format changes.
- [HandleChangeStreamIsActive](iouservideostream/handlechangestreamisactive.md)
  The system calls this virtual method when the stream active state changes.
- [DeviceSampleRateChanged](iouservideostream/devicesampleratechanged.md)
  Call to update stream formats when the owning video device changes sample rate
### Working with video buffers
- [GetBufferCount](iouservideostream/getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](iouservideostream/getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
  Add a buffer to a video stream.
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.
### Working with channels
- [SetStartingChannel](iouservideostream/setstartingchannel.md)
  Sets the starting channel of the stream.
- [GetStartingChannel](iouservideostream/getstartingchannel.md)
  Gets the starting channel of the stream.
### Working with queues
- [GetInputQueue](iouservideostream/getinputqueue.md)
  Gets the buffer queue for the stream.
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [createQueues](iouservideostream/createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not.
- [destroyQueues](iouservideostream/destroyqueues.md)
  Releases the shared input and output queues.
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](iostreambufferqueue.md)
### Stream memory types
- [kIOStreamMemoryTypeBufferControl](kiostreammemorytypebuffercontrol.md)
- [kIOStreamMemoryTypeBufferData](kiostreammemorytypebufferdata.md)
- [kIOStreamMemoryTypeInputQueue](kiostreammemorytypeinputqueue.md)
- [kIOStreamMemoryTypeMask](kiostreammemorytypemask.md)
- [kIOStreamMemoryTypeOutputQueue](kiostreammemorytypeoutputqueue.md)

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream)*