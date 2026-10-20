# bLength

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The size of the descriptor.

**Availability**:
- macOS 10.12+

## Declaration

```c
uint8_t bLength;
```

## See Also

### Getting the Properties
- [bDescriptorType](./api-1646372-bdescriptortype.md)
  The type of the descriptor.
- [bDevCapabilityType](./api-1646365-bdevcapabilitytype.md)
  The device capability descriptor type.
- [iAdditionalInfoURL](./api-1646386-iadditionalinfourl.md)
  The index of a string descriptor providing a URL for detailed information about the product and supported modes.
- [bNumberOfAlternateModes](./api-1646385-bnumberofalternatemodes.md)
  The number of alternative supported modes.
- [bPreferredAlternateMode](./api-1646361-bpreferredalternatemode.md)
  The index of the preferred alternative mode.
- [vCONNPower](./api-1646367-vconnpower.md)
  The power that the adapter needs for full functionality.
- [bmConfigured](./api-1646380-bmconfigured.md)
  A value that indicates the state of the alternative modes.
- [bcdVersion](./api-1792100-bcdversion.md)
  The billboard capability version number.
- [bAdditionalFailureInfo](./api-1792101-badditionalfailureinfo.md)
  A value that indicates additional information on failures.
- [bReserved](./api-1646357-breserved.md)
  Reserved for future use.
- [pAltConfigurations](./api-1646374-paltconfigurations.md)
  An array of alternative configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboard/1646375-blength)*