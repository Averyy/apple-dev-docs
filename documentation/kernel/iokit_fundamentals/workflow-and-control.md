# Workflow and Control

**Framework**: Kernel

## Topics

### Work Loops
- [IOWorkLoop](ioworkloop.md)
### Timers
- [IOTimerEventSource](iotimereventsource.md)
  Time based event source mechanism.
- [IOWatchDogTimer](iowatchdogtimer.md)
- [IOGetTime](1575332-iogettime.md)
- [IOTimeStampConstant](1535203-iotimestampconstant.md)
- [IOTimeStampEndConstant](1535232-iotimestampendconstant.md)
- [IOTimeStampStartConstant](1535234-iotimestampstartconstant.md)
### Sleep
- [IODelay](1575328-iodelay.md)
  Spin delay for a number of microseconds.
- [IOPause](1575333-iopause.md)
  Spin delay for a number of nanoseconds.
- [IOSleep](1575320-iosleep.md)
  Sleep the calling thread for a number of milliseconds.
- [IOSleepWithLeeway](1575303-iosleepwithleeway.md)
### Dispatch Queues
- [IODispatchQueueInterface](iodispatchqueueinterface.md)
- [IODispatchSourceInterface](iodispatchsourceinterface.md)
- [IODispatchQueue](iodispatchqueue.md)
### Data Queues
- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
- [IODataQueueDispatchSourceInterface](iodataqueuedispatchsourceinterface.md)
- [IODataQueue](iodataqueue.md)
  A generic queue designed to pass data from the kernel to a user process.
### Output Queues
- [IOGatedOutputQueue](iogatedoutputqueue.md)
  An extension of an IOBasicOutputQueue.
- [IOBasicOutputQueue](iobasicoutputqueue.md)
  A concrete implementation of an IOOutputQueue.
- [IOOutputQueue](iooutputqueue.md)
  A packet queue that supports multiple producers and a single consumer.
### Notifications
- [IOServiceNotificationDispatchSource](ioservicenotificationdispatchsource.md)
- [IOServiceNotificationDispatchSourceInterface](ioservicenotificationdispatchsourceinterface.md)
- [IONotifier](ionotifier.md)
  An abstract base class defining common methods for controlling a notification request.
### Interrupts
- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](iofilterinterrupteventsource.md)
  Filtering varient of the $link IOInterruptEventSource.
- [IOInterruptEventSource](iointerrupteventsource.md)
  Event source for interrupt delivery to work-loop based drivers.
- [IOInterruptController](iointerruptcontroller.md)
- [PassthruInterruptController](passthruinterruptcontroller.md)
- [IOInterruptSource](iointerruptsource.md)
- [IOInterruptVector](iointerruptvector.md)
### Base Types
- [IOCommandPool](iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommandGate](iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IOCommand](iocommand.md)
  This class is an abstract class which represents an I/O command.
- [IODispatchSource](iodispatchsource.md)
- [IOEventSource](ioeventsource.md)
  Abstract class for all work-loop event sources.

## See Also

- [Memory](iokit_fundamentals/memory.md)
  Allocate, map, free, and manage memory in the kernel. 
- [Locks](iokit_fundamentals/locks.md)
- [Data Types](libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokit_fundamentals/workflow_and_control)*