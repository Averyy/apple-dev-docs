# CaptureComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows your component to capture another component. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
Component CaptureComponent(Component capturedComponent, Component capturingComponent);
```

## Return Value

A new component identifier. Your component can use this new identifier to refer to the captured component. For example, your component can open the captured component by providing this identifier to the [`OpenComponent`](./api-1516607-opencomponent.md) structure. Your component must provide this identifier to the [`UncaptureComponent`](./api-1516646-uncapturecomponent.md) function to specify the component to be restored to the search list. If the component you wish to capture is already captured, the component identifier is set to `NULL`. See the description of the `Component` data type.

## Discussion

Typically, your component captures another component when you want to override all or some of the features provided by a component or to provide new features. For example, a component called NewMath might capture a component called OldMath. Suppose the NewMath component provides a new function, `DoExponent`. Whenever NewMath gets an exponent request, it can handle the request itself. For all other requests, NewMath might call the OldMath component to perform the request.

After capturing a component, your component might choose to target a particular instance of the captured component.

In response to this function, the Component Manager removes the specified component from the list of available components. As a result, applications cannot retrieve information about the captured component or gain access to it. Current clients of the captured component are not affected by this function. 

## Parameters

- `capturedComponent`: The component to be captured. Your component can obtain this identifier from the [`FindNextComponent`](./api-1516552-findnextcomponent.md) function or from the component registration functions. You can use a component instance here, but you must coerce the data type appropriately. 
- `capturingComponent`: Your component. Note that you can use the component instance (appropriately coerced) that your component received in its open request in this parameter.

## See Also

### Capturing Components
- [UncaptureComponent](./api-1516646-uncapturecomponent.md)
  Allows your component to uncapture a previously captured component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516357-capturecomponent)*