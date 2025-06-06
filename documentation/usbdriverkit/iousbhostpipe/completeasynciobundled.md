# CompleteAsyncIOBundled

**Framework**: USBDriverKit  
**Kind**: method

Handles the completion of an asynchronous bundled transfer.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void CompleteAsyncIOBundled(OSAction * action, uint32_t ioCompletionIndex, uint32_t ioCompletionCount, const uint32_t actualByteCountArray[16], int actualByteCountArrayCount, const kern_return_t statusArray[16], int statusArrayCount);
```

#### Discussion

Implement a custom version of this method and use the [`TYPE`](https://developer.apple.com/documentation/DriverKit/TYPE) macro to let the system know that your method conforms to this prototype.

When a call to [`AsyncIOBundled`](iousbhostpipe/asynciobundled.md) finishes, the system calls your completion method to report the number of successful transfers. The `ioCompletionCount` parameter contains the number of successful transfers, starting at position `ioCompletionIndex` in the pipe’s memory descriptor ring.  The completion count is at least 1, and no more than the value of [`kIOUSBHostPipeBundlingMax`](kiousbhostpipebundlingmax.md). The `actualByteCountArray` and `statusArray` parameters contain the length of each buffer and the status of each request.

## Parameters

- `action`: A pointer to the   object of the request.
- `ioCompletionIndex`: The index of the first ring element that the system transferred.
- `ioCompletionCount`: The number of successfully transferred elements.
- `actualByteCountArray`: An array of integers, each of which contains the amount of data that the method transferred for an element. The first integer in the array contains the length of the buffer for the element at the index  . The next integer contains the length of the buffer for the next element in the ring, and so on.
- `actualByteCountArrayCount`: The number of elements in the   parameter. The value in this parameter must match the value in  .
- `statusArray`: An array of status values for each transfer.
- `statusArrayCount`: The number of elements in the   parameter. The value in this parameter must match the value in  .

## See Also

- [kern_return_t CreateMemoryDescriptorRing(uint32_t size);](IOUSBHostPipe/CreateMemoryDescriptorRing.md)
- [kern_return_t SetMemoryDescriptor(IOMemoryDescriptor * memoryDescriptor, uint32_t index);](IOUSBHostPipe/SetMemoryDescriptor.md)
- [AsyncIOBundled](iousbhostpipe/asynciobundled.md)
  Enqueues a contiguous group of requests from the descriptor ring.
- [Bundling Constants](bundling_constants-enum.md)
  Constants associated with bulk I/O transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/completeasynciobundled)*