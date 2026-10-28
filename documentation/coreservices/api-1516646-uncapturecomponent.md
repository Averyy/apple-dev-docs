# UncaptureComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows your component to uncapture a previously captured component.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr UncaptureComponent(Component aComponent);
```

## Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Discussion

This function restores the specified component to the list of available components. Applications can then access the component and retrieve information about the component using Component Manager functions. 

## Parameters

- `aComponent`: The component to be uncaptured. Your component obtains this identifier from the [`CaptureComponent`](./api-1516357-capturecomponent.md) function. You can use a component instance here, but you must coerce the data type appropriately. 

## See Also

### Capturing Components
- [CaptureComponent](./api-1516357-capturecomponent.md)
  Allows your component to capture another component. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516646-uncapturecomponent)*