# kIOPMAssertionHumanReadableReasonKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Optional key that provides a localizable string for macOS to display PM Assertions in the GUI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionHumanReadableReasonKey
```

#### Discussion

The caller should specify this string in [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md). If present, macOS may display this string, localized to the user's language, to explain changes in system behavior caused by the assertion.

If set, the caller must also specify a bundle path for the key [`kIOPMAssertionLocalizationBundlePathKey`](./kiopmassertionlocalizationbundlepathkey.md) The bundle at that path should contain localization info for the specified string.

This key may be specified in the dictionary passed to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md).

This key may be present in the dictionary returned from [`IOPMAssertionCopyProperties`](./api-1557066-iopmassertioncopyproperties.md).

Describe your assertion as thoroughly as possible. See these other keys that can you can set to add explanation to an assertion: REQUIRED [`kIOPMAssertionNameKey`](./kiopmassertionnamekey.md) OPTIONAL [`kIOPMAssertionDetailsKey`](./kiopmassertiondetailskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertionhumanreadablereasonkey)*