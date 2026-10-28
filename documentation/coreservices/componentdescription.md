# ComponentDescription

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct ComponentDescription {
    ...
} ComponentDescription;
```

## Overview

The ComponentDescription structure identifies the characteristics of a component, including the type of services offered by the component and its manufacturer.

Applications and components use component description structures in different ways. An application that uses components specifies the selection criteria for a component in a component description structure. The functions  [`FindNextComponent`](./api-1516552-findnextcomponent.md) ,  [`CountComponents`](./api-1516515-countcomponents.md) , and  [`GetComponentInfo`](./api-1516438-getcomponentinfo.md)  all use the component description structure to specify the criteria for their search.

A component uses the component description structure to specify its registration information and capabilities and identify itself to the Component Manager. If your component is stored in a component resource, the information in the component description structure must be part of that resource. See the description of the component ‘thng’ resource. If you have developed an application that registers your component, that application must supply a component description structure to the  [`RegisterComponent`](./api-1516537-registercomponent.md)  function. See “Registering Components” for information about registering components.

The `ComponentDescription` data type defines the component description structure. Note that the valid values of fields in the component description structure are determined by the component type specification. For example, all image compressor components must use the `componentSubType` field to specify the compression algorithm used by the compressor. 

## Topics

### Instance Properties
- [componentFlags](./componentdescription/api-1516652-componentflags.md)
  A 32-bit field that provides additional information about a particular component.
- [componentFlagsMask](./componentdescription/api-1516402-componentflagsmask.md)
  A 32-bit field that indicates which flags in the `componentFlags` field are relevant to a particular component search operation. 
- [componentManufacturer](./componentdescription/api-1516444-componentmanufacturer.md)
  A four-character code that identifies the manufacturer of the component. 
- [componentSubType](./componentdescription/api-1516568-componentsubtype.md)
  A four-character code that identifies the subtype of the component. 
- [componentType](./componentdescription/api-1516339-componenttype.md)
  A four-character code that identifies the type of component. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentdescription)*