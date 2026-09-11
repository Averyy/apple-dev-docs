# init

**Framework**: VideoDriverKit  
**Kind**: method

Initializes a video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_acquirable, OSString *in_box_uid);
```

#### Return Value

True on success.

#### Discussion

Always pass in the IOUserVideoDriver and arguments. init() will always return false;

## Parameters

- `in_is_acquirable`: Bool value
- `in_box_uid`: An OSString pointer for the box unique identifier

## See Also

- [Create](iouservideobox/create.md)
  Static factory method to allocate and initialize an IOUserVideoBox.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/init)*