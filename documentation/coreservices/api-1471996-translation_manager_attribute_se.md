# Translation Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Translation Manager.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltTranslationAttr](./api-1471996-translation_manager_attribute_se/gestalttranslationattr.md)
  The `Gestalt` selector you pass to determine which Translation Manager attributes are present.
- [gestaltTranslationMgrExists](./api-1471996-translation_manager_attribute_se/gestalttranslationmgrexists.md)
  If `true`, the Translation Manager is present.
- [gestaltTranslationMgrHintOrder](./api-1471996-translation_manager_attribute_se/gestalttranslationmgrhintorder.md)
  In earlier versions of the Translation Manager, the scrap hints in the `DoTranslateScrapProcPtr` function were reversed. In later versions, this was fixed. If this bit is true, this bug fix is in effect.
- [gestaltTranslationPPCAvail](./api-1471996-translation_manager_attribute_se/gestalttranslationppcavail.md)
  If `true`, the PowerPC Translation Library is available, and you can call the Translation Manager from native PowerPC code.
- [gestaltTranslationGetPathAPIAvail](./api-1471996-translation_manager_attribute_se/gestalttranslationgetpathapiavail.md)
  If true, the functions `GetFileTranslationPath` and `GetPathTranslationDialog` are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471996-translation_manager_attribute_se)*