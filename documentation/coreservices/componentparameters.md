# ComponentParameters

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct ComponentParameters {
    ...
} ComponentParameters;
```

## Overview

The Component Manager uses the component parameters structure to pass information to your component about a request from an application. Functions which use this data type are  [`CallComponentFunction`](./api-1516603-callcomponentfunction.md) ,  [`CallComponentFunctionWithStorage`](./api-1516610-callcomponentfunctionwithstorage.md) , and  [`DelegateComponentCall`](./api-1516373-delegatecomponentcall.md).The information in this structure completely defines the request. Your component services the request as appropriate.

The `ComponentParameters` data type defines the component parameters structure. 

## Topics

### Instance Properties
- [flags](./componentparameters/api-1516638-flags.md)
  Reserved for use by Apple. 
- [padding](./componentparameters/api-1516573-padding.md)
- [paramSize](./componentparameters/api-1516330-paramsize.md)
  Specifies the number of bytes of parameter data for this request. The actual parameters are stored in the `params` field.
- [params](./componentparameters/api-1516563-params.md)
  An array that contains the parameters specified by the application that called your component. You can use the `CallComponentRoutine` or `CallComponentRoutineWithStorage` function to convert this array into a Pascal-style invocation of a subroutine in your component.
- [what](./componentparameters/api-1516601-what.md)
  Specifies the type of request. Component designers define the meaning of positive values and assign them to requests that are supported by components of a given type. Negative values are reserved for definition by Apple. See “Result Codes” for Apple-defined request code values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentparameters)*