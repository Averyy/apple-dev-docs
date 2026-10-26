# ComponentResourceExtension

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct ComponentResourceExtension {
    ...
} ComponentResourceExtension;
```

#### Overview

You can optionally include in your component resource the information defined by the `ComponentResourceExtension` data type: 

## Topics

### Instance Properties
- [componentIconFamily](./componentresourceextension/api-1516662-componenticonfamily.md)
  The resource ID of an icon family. You can provide an icon family in addition to the icon provided in the `componentIcon` field. Note that members of this icon family are not used by the Finder you supply an icon family only so that other components or applications can display your component’s icon in a dialog box if needed.
- [componentRegisterFlags](./componentresourceextension/api-1516519-componentregisterflags.md)
  A set of flags containing additional registration information. See [Component Resource Extension Flags](./api-1516650-component_resource_extension_fla.md) for the flag values.
- [componentVersion](./componentresourceextension/api-1516636-componentversion.md)
  The version number of the component. If you specify the `componentDoAutoVersion` flag in `componentRegisterFlags`, the Component Manager must obtain the version number of your component when your component is registered. Either you can provide a version number in your component’s resource, or you can specify a value of 0 for its version number. If you specify 0, the Component Manager sends your component a version request to get the version number of your component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentresourceextension)*