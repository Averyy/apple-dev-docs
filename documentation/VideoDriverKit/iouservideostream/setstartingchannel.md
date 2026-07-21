# SetStartingChannel

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetStartingChannel(uint32_t in_starting_channel);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the starting channel of the IOUserVideoStream

Starting channel can be changed dynamically.  A notification will be sent to the host to update the object state if successful.

## Parameters

- `in_starting_channel`: uint32_t that specifies the first element in the owning device that corresponds to element one of this stream

## See Also

- [GetStartingChannel](iouservideostream/getstartingchannel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setstartingchannel)*