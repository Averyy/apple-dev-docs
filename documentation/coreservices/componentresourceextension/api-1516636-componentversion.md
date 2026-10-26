# componentVersion

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

The version number of the component. If you specify the `componentDoAutoVersion` flag in `componentRegisterFlags`, the Component Manager must obtain the version number of your component when your component is registered. Either you can provide a version number in your component’s resource, or you can specify a value of 0 for its version number. If you specify 0, the Component Manager sends your component a version request to get the version number of your component.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
SInt32 componentVersion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentresourceextension/1516636-componentversion)*