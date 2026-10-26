# kIOPMAssertionLocalizationBundlePathKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Refers to a CFURL, as a CFString, identifying the path to the caller's bundle, which contains localization info.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionLocalizationBundlePathKey
```

#### Discussion

The bundle must contain localizations for [`kIOPMAssertionHumanReadableReasonKey`](./kiopmassertionhumanreadablereasonkey.md)

This key may be specified in the dictionary passed to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md).

This key may be present in the dictionary returned from [`IOPMAssertionCopyProperties`](./api-1557066-iopmassertioncopyproperties.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertionlocalizationbundlepathkey)*