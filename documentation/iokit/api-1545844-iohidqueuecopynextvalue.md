# IOHIDQueueCopyNextValue

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Dequeues a retained copy of an element value from the head of an IOHIDQueue.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
IOHIDValueRef IOHIDQueueCopyNextValue(IOHIDQueueRef queue);
```

#### Return Value

Returns valid IOHIDValueRef if data is available.

#### Discussion

Because the value is a retained copy, it is up to the caller to release the value using CFRelease. Use with setValueCallback to avoid polling the queue for data.

## Parameters

- `queue`: IOHIDQueue object to be queried.

## See Also

### Miscellaneous
- [IOHIDQueueAddElement](./api-1545835-iohidqueueaddelement.md)
  Adds an element to the queue
- [IOHIDQueueContainsElement](./api-1545842-iohidqueuecontainselement.md)
  Queries the queue to determine if elemement has been added.
- [IOHIDQueueCopyNextValueWithTimeout](./api-1545832-iohidqueuecopynextvaluewithtimeo.md)
  Dequeues a retained copy of an element value from the head of an IOHIDQueue. This method will block until either a value is available or it times out.
- [IOHIDQueueCreate](./api-1545840-iohidqueuecreate.md)
  Creates an IOHIDQueue object for the specified device.
- [IOHIDQueueGetDepth](./api-1545833-iohidqueuegetdepth.md)
  Obtain the depth of the queue.
- [IOHIDQueueGetDevice](./api-1545839-iohidqueuegetdevice.md)
  Obtain the device associated with the queue.
- [IOHIDQueueGetTypeID](./api-1545836-iohidqueuegettypeid.md)
  Returns the type identifier of all IOHIDQueue instances.
- [IOHIDQueueRegisterValueAvailableCallback](./api-1545829-iohidqueueregistervalueavailable.md)
  Sets callback to be used when the queue transitions to non-empty.
- [IOHIDQueueRemoveElement](./api-1545838-iohidqueueremoveelement.md)
  Removes an element from the queue
- [IOHIDQueueScheduleWithRunLoop](./api-1545841-iohidqueueschedulewithrunloop.md)
  Schedules queue with run loop.
- [IOHIDQueueSetDepth](./api-1545846-iohidqueuesetdepth.md)
  Sets the depth of the queue. @disussion Set the appropriate depth value based on the number of elements contained in a queue.
- [IOHIDQueueStart](./api-1545843-iohidqueuestart.md)
  Starts element value delivery to the queue.
- [IOHIDQueueStop](./api-1545830-iohidqueuestop.md)
  Stops element value delivery to the queue.
- [IOHIDQueueUnscheduleFromRunLoop](./api-1545834-iohidqueueunschedulefromrunloop.md)
  Unschedules queue with run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1545844-iohidqueuecopynextvalue)*