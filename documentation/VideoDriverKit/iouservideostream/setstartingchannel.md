# SetStartingChannel

**Framework**: VideoDriverKit  
**Kind**: method

Sets the starting channel of the stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetStartingChannel(uint32_t in_starting_channel);
```

#### Discussion

Starting channel can be changed dynamically. The object sends a notification to the host to update the object state on success.

## Parameters

- `in_starting_channel`: The first element in the owning device that corresponds to element one of this stream.

## See Also

- [GetStartingChannel](iouservideostream/getstartingchannel.md)
  Gets the starting channel of the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setstartingchannel)*