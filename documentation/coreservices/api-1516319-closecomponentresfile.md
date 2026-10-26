# CloseComponentResFile

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Closes the resource file that your component opened previously with the `OpenComponentResFile` function. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr CloseComponentResFile(ResFileRefNum refnum);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Parameters

- `refnum`: The reference number that identifies the resource file to be closed. Your component obtains this value from the [`OpenComponentResFile`](./api-1516550-opencomponentresfile.md) function. Your component must close any open resource files before returning to the calling application. 

## See Also

### Accessing a Component’s Resource File
- [OpenAComponentResFile](./api-1516643-openacomponentresfile.md)
- [OpenComponentResFile](./api-1516550-opencomponentresfile.md)
  Allows your component to gain access to its resource file. 
- [GetComponentResource](./api-1516387-getcomponentresource.md)
- [GetComponentIndString](./api-1516616-getcomponentindstring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516319-closecomponentresfile)*