# CMMakeProfile

**Framework**: Application Services  
**Kind**: func

Makes a display or abstract profile by modifying an existing one.

## Declaration

```c
CMError CMMakeProfile (
   CMProfileRef prof,
   CFDictionaryRef spec
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The function `CMMakeProfile` adds appropriate tags to a profile to make a display or abstract profile based on a specification dictionary you supply. 

One key in the specification dictionary must be `"profileType"` with a CFString value of either `"abstractLab"`, `"displayRGB"` or `"displayID"`. 

The dictionary can optionally contain these keys-value pairs:

- `"description"`, with an associated CFString value
- `"copyright"`, with an associated CFString value

For a `profileType` key whose value is `"abstractLab"`, the dictionary can also contain the keys-value pairs listed in [Table 1](./api-1804920-cmmakeprofile.md#1966820).

| Key | Value | Comment |
| --- | --- | --- |
| `"gridPoints"` | A CFNumber (`SInt32`) that is an odd | Required |
| `"proc"` | A CFNumber (`SInt64`) coerced from a `LabToLabProcPtr` data type | Required |
| `"refcon"` | A CFNumber (`SInt64`) value coerced from a `void*` data type | Optional |

For a `profileType` key whose value is `"displayRGB"`, the dictionary can also contain the keys-value pairs listed in [Table 2](./api-1804920-cmmakeprofile.md#1966827).

| Key | Value | Comment |
| --- | --- | --- |
| `"targetGamma"` | A CFNumber (`Float`), for example, 1.8 | Optional |
| `"targetWhite"` | A CFNumber (`SInt32`), for example, 6500 | Optional |
| `"gammaR` | A CFNumber (`Float`), for example, 2.5 | Required |
| `"gammaG"` | A CFNumber (`Float`), for example, 2.5 | Required |
| `"gammaB"` | A CFNumber (`Float`), for example, 2.5 | Required |
| `"tableChans"` | A CFNumber (`SInt32`), for example, 1 or 3 | Optional |
| `"tableEntries"` | A CFNumber (`SInt32`), for example, 16 or 255 | Optional |
| `"tableEntrySize"` | A CFNumber (`SInt32`), for example,1 or 2 | Optional |
| `"tableData"` | A CFData (lut in RRRGGGBBB order) | Optional |
| `"phosphorRx"` | A CFNumber (`Float`) | Only if not supplying the `phospherSet` key. |
| `phosphorRy"` | A CFNumber (`Float`) | Only if not supplying the `phospherSet` key. |
| `phosphorGx"` | A CFNumber (`Float`) | Only if not supplying the `phospherSet` key. |
| `"phosphorGy"` | A CFNumber (`Float`) | Only if not supplying the `phospherSet` key. |
| `"phosphorBx"` | A CFNumber (`Float`) | Only if not supplying the `phospherSet` key. |
| `"phosphorBy"` | A CFNumber (`Float`) | Only if not supplying the `phospherSet` key. |
| `"phosphorSet"` | A CFString: "WideRGB", "700/525/450nm", "P22-EBU", "HDTV", "CCIR709", "sRGB", "AdobeRGB98" or "Trinitron" | Only if not supplying the phosphor R, G, B keys |
| `"whitePointx"` | A CFNumber (`Float`) | Only if not supplying a `whiteTemp` key |
| `"whitePointy"` | A CFNumber (`Float`) | Only if not supplying a `whiteTemp` key |
| `"whiteTemp"` | A CFNumber (`SInt32`), for example, 5000, 6500, or 9300 | Only if not supplying `whitePointx` and `whitePointy` keys |

For a `profileType` key whose value is `"displayID"`, the dictionary can also contain the keys-value pairs in [Table 3](./api-1804920-cmmakeprofile.md#1966832)

| Key | Value | Comment |
| --- | --- | --- |
| `"targetGamma"` | A CFNumber (`Float`), for example, 1.8 | Optional |
| `"targetWhite"` | A CFNumber (`SInt32`), for example, 6500 | Optional |
| `"displayID”` | A CFNumber (`SInt32`) | Required |

Optionally, the keys-value pairs s for a `profileType` key whose value is `"displayRGB"` can be provided to override the values from the display.

## Parameters

- `prof`: The profile to modify.
- `spec`: A dictionary that specifies the modifications to make to the profile supplied in the `prof` parameter.

## See Also

### Creating Profiles
- [CMNewProfile](./api-1804911-cmnewprofile.md)
  Creates a new profile and associated backing copy.
- [CWNewLinkProfile](./api-1804915-cwnewlinkprofile.md)
  Creates a device link profile based on the specified set of profiles.
- [NCWNewLinkProfile](./api-1804918-ncwnewlinkprofile.md)
  Obtains a profile reference for the specified by the profile location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804920-cmmakeprofile)*