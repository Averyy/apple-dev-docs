# VZVirtioQueue

**Framework**: Virtualization  
**Kind**: class

A Virtio queue.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZVirtioQueue
```

#### Overview

A `VZVirtioQueue` represents a virtqueue (Virtio queue) that belongs to a Virtio device. A virtqueue provides a mechanism for bulk data transport on Virtio devices, that facilitate device operations. For more information about how virtqueues work, see the [`Virtio specification`](https://developer.apple.comhttps://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.html).

Don’t instantiate `VZVirtioQueue` objects directly. Once you have created and configured a [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md), you can access the Virtio queues belonging to that device through the [`queue(at:)`](vzcustomvirtiodevice/queue(at:).md) method.

When the device receives a notification from the guest, the framework provides the queue with which the framework associates the notification as an argument when the framework calls [`customVirtioDevice(_:didReceiveNotificationFor:)`](vzcustomvirtiodevicedelegate/customvirtiodevice(_:didreceivenotificationfor:).md).

## Topics

### Instance Properties
- [var queueIndex: UInt16](vzvirtioqueue/queueindex.md)
  The index for this queue.
- [var queueSize: UInt16](vzvirtioqueue/queuesize.md)
  Size of this queue.
### Instance Methods
- [func nextElement() -> VZVirtioQueueElement?](vzvirtioqueue/nextelement.md)
  Gets the next element in this queue, if any.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZVirtioQueueElement](vzvirtioqueueelement.md)
  A unit of work on a Virtio queue, also known as a descriptor chain.
- [class VZVirtioQueueElement](vzvirtioqueueelement.md)
  A unit of work on a Virtio queue, also known as a descriptor chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueue)*