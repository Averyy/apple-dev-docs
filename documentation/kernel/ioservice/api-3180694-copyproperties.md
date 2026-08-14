# CopyProperties

**Framework**: Kernel  
**Kind**: instm

Returns the registry properties associated with the current service. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t CopyProperties(OSDictionary **properties, OSDispatchMethod supermethod);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

## Parameters

- `properties`: A variable for storing the properties. On return, the variable contains a dictionary with the properties, or `NULL` if the service has no registered properties. If this method returns a valid dictionary, you are responsible for releasing that dictionary when you are finished with it.  It is a programmer error to specify `NULL` or an invalid pointer for this parameter.

## See Also

- [- SetProperties](../driverkit/ioservice/setproperties.md)
  Sends the dictionary of properties to the current service object.
- [- SearchProperty](../driverkit/ioservice/searchproperty.md)
  Searches for a property with the specified name in the current service or one of its parent services, and returns the corresponding value. 
- [IOPropertyName](../driverkit/iopropertyname.md)
  A string type for specifying the name of a property in the system's registry. 
- [IORegistryPlaneName](../driverkit/ioregistryplanename.md)
  A string type for specifying the name of a plane in the system's registry. 
- [Search Options](../driverkit/3325572-search_options.md)
  Options to apply when searching for registry properties. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180694-copyproperties)*