# IOHIDQueueContainsElement

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Queries the queue to determine if elemement has been added.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
Boolean IOHIDQueueContainsElement(IOHIDQueueRef queue, IOHIDElementRef element);
```

## Return Value

Returns true or false depending if element is present.

## Parameters

- `queue`: IOHIDQueue object to be queried.
- `element`: Element to be queried.

## See Also

### Miscellaneous
- [IOHIDQueueAddElement](./api-1545835-iohidqueueaddelement.md)
  Adds an element to the queue
- [IOHIDQueueCopyNextValue](./api-1545844-iohidqueuecopynextvalue.md)
  Dequeues a retained copy of an element value from the head of an IOHIDQueue.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1545842-iohidqueuecontainselement)*