# SetTerminalType

**Framework**: VideoDriverKit  
**Kind**: method

Sets the terminal type of the stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetTerminalType(IOUserVideoStreamTerminalType in_terminal_type);
```

#### Discussion

You can change the terminal type dynamically. On success, the system sends a notification to the host to update the object state.

## See Also

- [GetTerminalType](iouservideostream/getterminaltype.md)
  Gets the terminal type of the stream.
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)
  The terminal type of video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setterminaltype)*