# IOStream

**Framework**: Kernel  
**Kind**: cl

A class representing a stream of data buffers passed from kernel to user space and back again.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IOStream : IOService
```

#### Overview

The IOStream class defines a mechanism for moving buffers of data from kernel space to user space or vice-versa. The policy for which direction the data flows and the nature of the data is left up the the implementer of the driver which uses IOStream.

Although it is expected that the client of an IOStream will be in user space, this is not required.

References to "output" mean "from the IOStream to the user client", and "input" means "from the user client to the IOStream."

## Topics

### Stream control
- [getStreamMode](iostream/1809626-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [setStreamMode](iostream/1809631-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iostream/1809638-startstream.md)
  Start sending data on a stream.
- [stopStream](iostream/1809642-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iostream/1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.
### Queueing and dequeueing buffers
- [dequeueInputEntry](iostream/1809653-dequeueinputentry.md)
- [enqueueOutputBuffer](iostream/1809665-enqueueoutputbuffer.md)
  A convenience method for enqueueing a buffer.
- [enqueueOutputEntry](iostream/1809670-enqueueoutputentry.md)
### Opening and closing streams
- [handleClose](iostream/1809680-handleclose.md)
  The handleClose method destroys the shared input and output queues.
- [handleOpen](iostream/1809688-handleopen.md)
  The handleOpen() method relies on the default IOService behavior to ensure that only one client has the stream open at a time. The shared input and output queues are created at open time.
### Managing user clients
- [newUserClient](iostream/1809695-newuserclient.md)
  See the documentation for the IOService method newUserClient.
### Managing shared queues
- [createQueues](iostream/1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [destroyQueues](iostream/1809709-destroyqueues.md)
  Releases the shared input and output queues.
- [getInputQueue](iostream/1809718-getinputqueue.md)
- [getInputQueueMemoryDescriptor](iostream/1809727-getinputqueuememorydescriptor.md)
- [getOutputQueue](iostream/1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](iostream/1809744-getoutputqueuememorydescriptor.md)
### Managing notifications
- [inputCallback](iostream/1809754-inputcallback.md)
  Input callback function to be implemented by a subclass;
- [inputSyncCallback](iostream/1809761-inputsynccallback.md)
  Input callback function to be implemented by a subclass.
### Managing notification ports
- [getInputPort](iostream/1809770-getinputport.md)
  Get the Mach port used to receive notifications from user space that a buffer has been added to the input queue.
- [getOutputPort](iostream/1809774-getoutputport.md)
  Get the Mach port used to send notifications to user space that a buffer has been added to the output queue.
- [sendOutputNotification](iostream/1809783-sendoutputnotification.md)
  Send a notification to the user client that data is available for reading on the output queue. This will result in the user's output handler being called, if they registered one.
- [setInputPort](iostream/1809793-setinputport.md)
  Set the Mach port used to receive notifications from user space that a buffer has been added to the input queue.
- [setOutputPort](iostream/1809801-setoutputport.md)
  Set the Mach port used to send notifications to user space that a buffer has been added to the output queue.
### Managing buffers in an IOStream
- [addBuffer](iostream/1809807-addbuffer.md)
  Add a buffer to an IOStream.
- [addBuffers](iostream/1809814-addbuffers.md)
- [getBufferCount](iostream/1809821-getbuffercount.md)
- [getBuffers](iostream/1809828-getbuffers.md)
  Get an array containing all the buffers in the stream.
- [getBufferWithID](iostream/1809834-getbufferwithid.md)
- [removeAllBuffers()](iostream/1809839-removeallbuffers.md)
- [removeAllBuffers()](iostream/1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBuffer *)](iostream/1809852-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
- [removeBuffer(IOStreamBufferID)](iostream/1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
### Creating IOStream objects
- [free](iostream/1809867-free.md)
- [initWithBuffers](iostream/1809875-initwithbuffers.md)
- [withBuffers](iostream/1809882-withbuffers.md)
### Instance Methods
- [- addBuffer](iostream/1589858-addbuffer.md)
- [- addBuffers](iostream/1589843-addbuffers.md)
- [- createQueues](iostream/1589877-createqueues.md)
- [- dequeueInputEntry](iostream/1589881-dequeueinputentry.md)
- [- destroyQueues](iostream/1589871-destroyqueues.md)
- [- enqueueOutputBuffer](iostream/1589872-enqueueoutputbuffer.md)
- [- enqueueOutputEntry](iostream/1589856-enqueueoutputentry.md)
- [- free](iostream/1589852-free.md)
- [- getBufferCount](iostream/1589838-getbuffercount.md)
- [- getBufferWithID](iostream/1589840-getbufferwithid.md)
- [- getBuffers](iostream/1589876-getbuffers.md)
- [- getInputPort](iostream/1589874-getinputport.md)
- [- getInputQueue](iostream/1589835-getinputqueue.md)
- [- getInputQueueMemoryDescriptor](iostream/1589879-getinputqueuememorydescriptor.md)
- [- getMetaClass](iostream/1589853-getmetaclass.md)
- [- getOutputPort](iostream/1589854-getoutputport.md)
- [- getOutputQueue](iostream/1589847-getoutputqueue.md)
- [- getOutputQueueMemoryDescriptor](iostream/1589862-getoutputqueuememorydescriptor.md)
- [- getStreamMode](iostream/1589841-getstreammode.md)
- [- handleClose](iostream/1589873-handleclose.md)
- [- handleOpen](iostream/1589839-handleopen.md)
- [- init](iostream/1589846-init.md)
- [- initWithBuffers](iostream/1589845-initwithbuffers.md)
- [- inputCallback](iostream/1589831-inputcallback.md)
- [- inputSyncCallback](iostream/1589880-inputsynccallback.md)
- [- newUserClient](iostream/1589851-newuserclient.md)
- [- removeAllBuffers](iostream/1589878-removeallbuffers.md)
- [- removeBuffer](iostream/1589833-removebuffer.md)
- [- removeBuffer](iostream/3516782-removebuffer.md)
- [- sendOutputNotification](iostream/1589861-sendoutputnotification.md)
- [- setInputPort](iostream/1589836-setinputport.md)
- [- setOutputPort](iostream/1589866-setoutputport.md)
- [- setStreamMode](iostream/1589870-setstreammode.md)
- [- startStream](iostream/1589837-startstream.md)
- [- stopStream](iostream/1589863-stopstream.md)
- [- suspendStream](iostream/1589867-suspendstream.md)
### Type Methods
- [+ withBuffers](iostream/1589868-withbuffers.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOSharedDataQueue](ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOSharedInterruptController](iosharedinterruptcontroller.md)
- [IOUserClient](iouserclient.md)
  Provides a basis for communication between client applications and I/O Kit objects.
- [IOStreamUserClient](iostreamuserclient.md)
- [IOStreamBuffer](iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream)*