# queue(at:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Returns Virtio queue at the specified index that belongs to this device.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func queue(at index: UInt16) -> VZVirtioQueue?
```

```objc
- (VZVirtioQueue *) queueAtIndex:(uint16_t) index;
```

## Return Value

The [`VZVirtioQueue`](../vzvirtioqueue.md) object at the specified index, or `nil` if the index is invalid or the guest driver has disabled the queue.

## Discussion

The framework sets up the virtqueues (Virtio queues) when the guest driver sets `DRIVER_OK`; this call returns a valid result only after the framework calls [`customVirtioDeviceDidAcceptDriverOk(_:)`](../vzcustomvirtiodevicedelegate/customvirtiodevicedidacceptdriverok%28_%29.md).

## Parameters

- `index`: The index of the [`VZVirtioQueue`](../vzvirtioqueue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/queue(at:))*