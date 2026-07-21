# SetTerminalType

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetTerminalType(IOUserVideoStreamTerminalType in_terminal_type);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the terminal type of the IOUserVideoStream

Terminal type can be changed dynamically.  A notification will be sent to the host to update the object state if successful.

## See Also

- [GetTerminalType](iouservideostream/getterminaltype.md)
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setterminaltype)*