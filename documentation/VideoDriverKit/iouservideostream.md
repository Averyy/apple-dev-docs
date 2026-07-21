# IOUserVideoStream

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoStream;
```

#### Overview

IOUserVideoStream is a subclass of IOUserVideoObject. IOUserVideoDevice’s own IOUserVideoStream’s. IOUserVideoStream’s allocate memory descriptors that the host uses for running IO. Changes to the owning IOUserVideoDevice will potentially update formats on the underlying IOUserVideoStream.

## Topics

### Creating a video stream
- [Create](iouservideostream/create.md)
- [init](iouservideostream/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
### Freeing a video stream
- [free](iouservideostream/free.md)
### Getting information about the class
- [GetClassID](iouservideostream/getclassid.md)
- [GetBaseClassID](iouservideostream/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Performing I/O
- [StartIO](iouservideostream/startio.md)
- [StopIO](iouservideostream/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [InputNotification](iouservideostream/inputnotification.md)
### Working with stream formats
- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)
### Working with stream terminals
- [SetTerminalType](iouservideostream/setterminaltype.md)
- [GetTerminalType](iouservideostream/getterminaltype.md)
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)
### Working with memory descriptors
- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)
- [GetMemoryObjectID](iouservideostream/getmemoryobjectid.md)
### Managing stream changes
- [HandleChangeCurrentStreamFormat](iouservideostream/handlechangecurrentstreamformat.md)
- [HandleChangeStreamIsActive](iouservideostream/handlechangestreamisactive.md)
- [DeviceSampleRateChanged](iouservideostream/devicesampleratechanged.md)
### Working with video buffers
- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferList](iouservideostream/getbufferlist.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)
### Working with channels
- [SetStartingChannel](iouservideostream/setstartingchannel.md)
- [GetStartingChannel](iouservideostream/getstartingchannel.md)
### Working with queues
- [GetInputQueue](iouservideostream/getinputqueue.md)
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
- [createQueues](iouservideostream/createqueues.md)
- [destroyQueues](iouservideostream/destroyqueues.md)
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
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