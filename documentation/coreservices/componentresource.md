# ComponentResource

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct ComponentResource {
    ...
} ComponentResource;
```

## Overview

The `ComponentResource` data type defines the structure of a component resource. You can also optionally append to the end of this structure the information defined by the  [`ComponentResourceExtension`](./componentresourceextension.md)  data type. 

## Topics

### Instance Properties
- [cd](./componentresource/api-1516401-cd.md)
  A [`ComponentDescription`](./componentdescription.md) structure that specifies the characteristics of the component. 
- [component](./componentresource/api-1516623-component.md)
  A resource specification structure that specifies the type and ID of the component code resource. The `resType` field of the resource specification structure may contain any value. The component’s main entry point must be at offset 0 in the resource. 
- [componentIcon](./componentresource/api-1516543-componenticon.md)
  A resource specification structure that specifies the resource type and ID for the icon for a component. Component icons are stored as 32-by-32 bit maps. Typically, the icon is stored in a resource of type `'ICON'`. Note that this icon is not used by the Finder you supply an icon only so that other components or applications can display your component’s icon in a dialog box if needed.
- [componentInfo](./componentresource/api-1516441-componentinfo.md)
  A resource specification structure that specifies the resource type and ID for the information string that describes the component. This is a Pascal string. Typically, the information string is stored in a resource of type `'STR'`. You might use the information stored in this resource in a Get Info dialog box.
- [componentName](./componentresource/api-1516658-componentname.md)
  A resource specification structure that specifies the resource type and ID for the name of the component. This is a Pascal string. Typically, the name is stored in a resource of type `'STR '`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentresource)*