# PropertiesChanged

**Framework**: VideoDriverKit  
**Kind**: method

This method informs the host when the state of an driver’s object changes.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t PropertiesChanged(IOUserVideoObjectID in_object_id, IOUserVideoObjectPropertySelector *in_properties, uint32_t in_num_properties);
```

#### Return Value

A kern_return_t indicating success or failure.

#### Discussion

For device objects, this method is only used for state changes that don’t affect IO or the structure of the device.

## Parameters

- `in_properties`: An array of IOUserVideoObjectPropertySelectors for the changed properties.
- `in_num_properties`: The number of elements in the in_properties array.

## See Also

- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.
- [IOUserVideoObjectPropertySelector](videodriverkit/iouservideoobjectpropertyselector.md)
  A four character code which, along with the scope and element, specifies a specific piece of information about a video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/propertieschanged)*