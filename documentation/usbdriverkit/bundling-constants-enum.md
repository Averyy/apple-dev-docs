# Bundling Constants

**Framework**: USBDriverKit

Constants associated with bulk I/O transfers.

## Topics

### Bundling Options
- [kIOUSBHostPipeBundlingMax](kiousbhostpipebundlingmax.md)
  The maximum number of elements to transfer in one bundled I/O call.

## See Also

- [kern_return_t CreateMemoryDescriptorRing(uint32_t size);](IOUSBHostPipe/CreateMemoryDescriptorRing.md)
- [kern_return_t SetMemoryDescriptor(IOMemoryDescriptor * memoryDescriptor, uint32_t index);](IOUSBHostPipe/SetMemoryDescriptor.md)
- [AsyncIOBundled](iousbhostpipe/asynciobundled.md)
  Enqueues a contiguous group of requests from the descriptor ring.
- [CompleteAsyncIOBundled](iousbhostpipe/completeasynciobundled.md)
  Handles the completion of an asynchronous bundled transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/bundling_constants-enum)*