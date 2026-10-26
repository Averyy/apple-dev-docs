# DelegateComponentCall

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows your component to pass on a request to a specified component. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
ComponentResult DelegateComponentCall(ComponentParameters *originalParams, ComponentInstance ci);
```

#### Return Value

The component result returned by the specified component. 

#### Discussion

Your component may supplement its capabilities by using the services of another component to directly satisfy application requests using this function. For example, you might want to create two similar components that provide different levels of service to applications. Rather than completely implementing both components, you could design one to rely on the capabilities of the other. In this manner, you have to implement only that portion of the more capable component that provides additional services.

You may also invoke the services of another component using the standard mechanisms used by applications. The Component Manager then passes the requests to the appropriate component, and your component receives the results of those requests.

Your component must open a connection to the component to which the requests are to be passed. Your component must close that connection when it has finished using the services of the other component.

Your component should never use this function with open or close requests from the Component Manager—always use the `OpenComponent` and  [`CloseComponent`](./api-1516436-closecomponent.md)  functions to manage connections with other components. 

## Parameters

- `originalParams`: A pointer to the [`ComponentParameters`](./componentparameters.md) structure provided to your component by the Component Manager. 
- `ci`: The component instance that is to process the request. The Component Manager provides a component instance to your component when it opens a connection to another component with the [`OpenComponent`](./api-1516607-opencomponent.md) or [`OpenDefaultComponent`](./api-1516523-opendefaultcomponent.md) function. You must specify a component instance; this function does not accept a component identifier. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516373-delegatecomponentcall)*