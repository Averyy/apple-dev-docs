# Component Manager

**Framework**: Core Services  
**Role**: API Collection

Find and use components in your app or add custom components to system-provided services, such as QuickTime and Core Audio. 

> **Deprecated**: The Component Manager is deprecated in macOS 10.8 and later.  If your app defines custom components to extend functionality, you can instead create a custom a plug-in to replicate the functionality you need. For more information, see [Code Loading Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/LoadingCode.html#//apple_ref/doc/uid/10000052i).  If your app loads audio units and audio codecs, use Audio Component Services instead. For more information, see `Audio Component Services`.

## Topics

### Result Codes
- [var invalidComponentID: Int](../invalidcomponentid.md)
  Invalid component ID.
- [var validInstancesExist: Int](../validinstancesexist.md)
  This component has open connections.
- [var componentNotCaptured: Int](../componentnotcaptured.md)
  This component has not been captured.
- [var componentDontRegister: Int](../componentdontregister.md)
- [var unresolvedComponentDLLErr: Int](../unresolvedcomponentdllerr.md)
- [var retryComponentRegistrationErr: Int](../retrycomponentregistrationerr.md)
- [var badComponentSelector: Int](../badcomponentselector.md)
  Component does not support the specified request code.
- [var badComponentInstance: Int](../badcomponentinstance.md)
  Invalid component  passed to Component Manager.

## See Also

### Managers
- [Gestalt Manager](./gestalt_manager.md)
  Investigate the operating environment of your app.
- [Text Encoding Conversion Manager](./text_encoding_conversion_manager.md)
  Handle text encoding conversion between apps and transfer text across different platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/component_manager)*