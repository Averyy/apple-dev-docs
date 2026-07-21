# PropertiesChanged

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t PropertiesChanged(IOUserVideoObjectID in_object_id, IOUserVideoObjectPropertySelector *in_properties, uint32_t in_num_properties);
```

#### Return Value

A kern_return_t indicating success or failure.

#### Discussion

This method informs the Host when the state of an driver’s object changes.

Note that for device objects, this method is only used for state changes that don’t affect IO or the structure of the device.

## Parameters

- `in_properties`: An array of IOUserVideoObjectPropertySelectors for the changed properties.
- `in_num_properties`: The number of elements in the in_properties array.

## See Also

- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
- [IOUserVideoObjectPropertySelector](videodriverkit/iouservideoobjectpropertyselector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/propertieschanged)*