# IOHIDQueue.h

**Framework**: IOKit  
**Role**: API Collection

#### Overview

IOHIDQueue defines an object used to queue values from input parsed items (IOHIDElement) contained within a Human Interface Device (HID) object. This object is useful when you need to keep track of all values of an input element, rather than just the most recent one. IOHIDQueue is a CFType object and as such conforms to all the conventions expected such object.

IOHIDQueue should be considered optional and is only useful for working with complex input elements. These elements include those whose length are greater than sizeof(CFIndex) or elements that are duplicate items. Whenever possible please defer to using IOHIDManagerRegisterInputValueCallback or IOHIDDeviceRegisterInputValueCallback.

** Note:**Absolute element values (based on a fixed origin) will only be placed on a queue if there is a change in value.

This documentation assumes that you have a basic understanding of the material contained in [Introduction to Accessing Hardware From Applications](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Intro/AH_Intro.html#//apple_ref/doc/uid/TP40002714).

All of the information described in this document is contained in the header file `IOHIDQueue.h` found at `/System/Library/Frameworks/IOKit.framework/Headers/hid/IOHIDQueue.h`.

##### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <IOKit/hid/IOHIDBase.h>

## Topics

### Miscellaneous
- [IOHIDQueueAddElement](./api-1545835-iohidqueueaddelement.md)
  Adds an element to the queue
- [IOHIDQueueContainsElement](./api-1545842-iohidqueuecontainselement.md)
  Queries the queue to determine if elemement has been added.
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
### Data Types
- [IOHIDQueueRef](./iohidqueueref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueue_h)*