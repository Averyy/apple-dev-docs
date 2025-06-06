# initWithBuffers

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool initWithBuffers(
 OSArray *buffers,
 IOStreamMode mode = kIOStreamModeOutput,
 IOItemCount queueLength = 0,
 OSDictionary *properties = 0);
```

## Parameters

- `mode`: The initial mode of the stream, either output, input, or input/output.
- `queueLength`: The nuber of queue entries to reserve in the input and output queue. Zero means to make the queues big enough to accommodate all the buffers at once.
- `properties`: A dictionary of properties which will be set on the stream.
- `buffers`: An array of IOStreamBuffer objects which will be the buffers for this stream.

## See Also

- [free](iostream/1809867-free.md)
- [withBuffers](iostream/1809882-withbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809875-initwithbuffers)*