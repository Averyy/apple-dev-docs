# AddCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Always returns `kIOReturnError` because a custom property cannot have a custom property.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
virtual kern_return_t AddCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

## See Also

### Working with custom properties
- [RemoveCustomProperty](./removecustomproperty.md)
  Always returns an error, because a custom property cannot have a custom property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/addcustomproperty)*