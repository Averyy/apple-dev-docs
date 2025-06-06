# enqueueOutputBuffer

**Framework**: Kernel  
**Kind**: instm

A convenience method for enqueueing a buffer.

## Declaration

```swift
virtual IOReturn enqueueOutputBuffer(
 IOStreamBuffer *buffer, 
 IOByteCount dataOffset = 0, 
 IOByteCount dataLength = 0, 
 IOByteCount controlOffset = 0, 
 IOByteCount controlLength = 0);
```

## Parameters

- `buffer`: 
- `dataOffset`: 
- `dataLength`: 
- `controlOffset`: 
- `controlLength`: 

## See Also

- [dequeueInputEntry](iostream/1809653-dequeueinputentry.md)
- [enqueueOutputEntry](iostream/1809670-enqueueoutputentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809665-enqueueoutputbuffer)*