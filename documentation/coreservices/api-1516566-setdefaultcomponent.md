# SetDefaultComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Changes the search order for registered components. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr SetDefaultComponent(Component aComponent, SInt16 flags);
```

## Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Discussion

Note that this function changes the search order for all applications. As a result, you should use this function carefully. 

## Parameters

- `aComponent`: The component which you wish moved to the front of the search chain. The order of the search chain influences which component the Component Manager selects in response to an application’s use of the [`OpenDefaultComponent`](./api-1516523-opendefaultcomponent.md) and [`FindNextComponent`](./api-1516552-findnextcomponent.md) functions. You can use a component instance here, but you must coerce the data type appropriately. 
- `flags`: A value specifying the control information governing the operation. The value of this parameter controls which component description fields the Component Manager examines during the reorder operation. Set the appropriate flags to 1 to define the fields that are examined during the reorder operation. See [Set Default Component Flags](./api-1516455-set_default_component_flags.md) for a description of the values you can use here. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516566-setdefaultcomponent)*