# Resource.PremiumResourceInfo

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Additional metadata that marks a resource as premium content that the reader originally sourced from the content hub.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Resource.PremiumResourceInfo
```

## Overview

It carries the watermarking terms attached to the resource.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.resource.premium-resource-info`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `asset_uuid` (string) *(required)*: The UUID of the premium resource’s asset in the media library, written as a standard UUID string. If the value isn’t a valid UUID, it’s ignored, and the resource then loses its media library association and its watermark information.
- `is_derived_asset` (boolean) *(required)*: Whether the resource was edited or otherwise derived from its original Content Hub data; if `false`, it’s the unmodified original.
- `may_need_watermark` (boolean) *(required)*: Whether the resource may be shown with a watermark for customers without an active subscription. When the document is read, the resource is treated as newly added, so such a customer can see a watermark on media that the original presentation showed without one.

## See Also

### Objects
- [object Resource.Base64EncodedResource](./resource.base64encodedresource.md)
  A resource whose bytes are carried as Base64 in the resource itself, so the JSON needs no companion files.
- [object Resource.IndirectResource](./resource.indirectresource.md)
  A resource whose bytes are stored in a separate file rather than in the JSON.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/resource.premiumresourceinfo)*