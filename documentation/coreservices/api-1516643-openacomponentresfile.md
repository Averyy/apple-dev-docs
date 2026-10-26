# OpenAComponentResFile

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr OpenAComponentResFile(Component aComponent, ResFileRefNum *resRef);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Parameters

- `aComponent`: 

## See Also

### Accessing a Component’s Resource File
- [OpenComponentResFile](./api-1516550-opencomponentresfile.md)
  Allows your component to gain access to its resource file. 
- [CloseComponentResFile](./api-1516319-closecomponentresfile.md)
  Closes the resource file that your component opened previously with the `OpenComponentResFile` function. 
- [GetComponentResource](./api-1516387-getcomponentresource.md)
- [GetComponentIndString](./api-1516616-getcomponentindstring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516643-openacomponentresfile)*