# Create

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoBox> Create(IOUserVideoDriver *in_driver, bool in_is_acquirable, OSString *in_box_uid);
```

#### Return Value

OSSharedPtr to an IOUserVideoBox if it was successfully allocated and initialized

#### Discussion

Static factory method to allocate and initialize an IOUserVideoBox.

If IOUserVideoBox is subclassed to override behavior, Create should not be used to allocate/initialize the custom subclass.

## Parameters

- `in_is_acquirable`: Bool value
- `in_box_uid`: An OSString pointer for the box unique identifier

## See Also

- [init](iouservideobox/init.md)
- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/create)*