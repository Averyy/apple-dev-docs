# TECPluginDispatchTable

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Contains version and signature information and pointers to the callback functions used by a text encoding converter plug-in.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct TECPluginDispatchTable {
    ...
} TECPluginDispatchTable;
```

## Topics

### Instance Properties
- [PluginClearContextInfo](./tecplugindispatchtable/api-1498524-pluginclearcontextinfo.md)
- [PluginClearSnifferContextInfo](./tecplugindispatchtable/api-1498588-pluginclearsniffercontextinfo.md)
- [PluginConvertTextEncoding](./tecplugindispatchtable/api-1498402-pluginconverttextencoding.md)
- [PluginDisposeEncodingConverter](./tecplugindispatchtable/api-1498432-plugindisposeencodingconverter.md)
- [PluginDisposeEncodingSniffer](./tecplugindispatchtable/api-1498546-plugindisposeencodingsniffer.md)
- [PluginFlushConversion](./tecplugindispatchtable/api-1498501-pluginflushconversion.md)
- [PluginGetCountAvailableSniffers](./tecplugindispatchtable/api-1498428-plugingetcountavailablesniffers.md)
- [PluginGetCountAvailableTextEncodingPairs](./tecplugindispatchtable/api-1498343-plugingetcountavailabletextencod.md)
- [PluginGetCountAvailableTextEncodings](./tecplugindispatchtable/api-1498514-plugingetcountavailabletextencod.md)
- [PluginGetCountDestinationTextEncodings](./tecplugindispatchtable/api-1498380-plugingetcountdestinationtextenc.md)
- [PluginGetCountMailTextEncodings](./tecplugindispatchtable/api-1498527-plugingetcountmailtextencodings.md)
- [PluginGetCountSubTextEncodings](./tecplugindispatchtable/api-1498410-plugingetcountsubtextencodings.md)
- [PluginGetCountWebTextEncodings](./tecplugindispatchtable/api-1498455-plugingetcountwebtextencodings.md)
- [PluginGetTextEncodingFromInternetName](./tecplugindispatchtable/api-1498475-plugingettextencodingfrominterne.md)
- [PluginGetTextEncodingInternetName](./tecplugindispatchtable/api-1498487-plugingettextencodinginternetnam.md)
- [PluginID](./tecplugindispatchtable/api-1498355-pluginid.md)
- [PluginNewEncodingConverter](./tecplugindispatchtable/api-1498583-pluginnewencodingconverter.md)
- [PluginNewEncodingSniffer](./tecplugindispatchtable/api-1498471-pluginnewencodingsniffer.md)
- [PluginSniffTextEncoding](./tecplugindispatchtable/api-1498411-pluginsnifftextencoding.md)
- [compatibleVersion](./tecplugindispatchtable/api-1498437-compatibleversion.md)
- [version](./tecplugindispatchtable/api-1498479-version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecplugindispatchtable)*