# create

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates the current queue.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*create)(void *self, uint32_t flags, uint32_t depth);
```

#### Return Value

Returns an IOReturn code.

## Parameters

- `flags`: Pass kIOHIDQueueOptionsTypeEnqueueAll option to force the IOHIDQueue to enqueue all events, relative or absolute, regardless of change.
- `depth`: The maximum number of elements in the queue before the oldest elements in the queue begin to be lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493412-create)*