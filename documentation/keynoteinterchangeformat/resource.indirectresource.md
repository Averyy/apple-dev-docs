# Resource.IndirectResource

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A resource whose bytes are stored in a separate file rather than in the JSON.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Resource.IndirectResource
```

## Overview

In a `.keyx` file, the `identifier` names a file in the archive’s `Data` directory. A name the reader can’t resolve is an error rather than an empty asset; what happens then depends on where the resource is used (see `Resource`).

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.resource.indirect-resource`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `Resource.IndirectResource` is 2.0.

  **Default**: `2.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): The name of the file inside the archive’s `Data` directory that contains the data for this resource. If missing, `filename` is used as the identifier. When no data can be found for it, the resource can’t be loaded (see `Resource` for what happens then).
- `filename` (string) *(required)*: The filename shown for the resource, including its filename extension, in the user interface. This value need not match `identifier`; see `identifier` for what happens when that’s absent. The extension is significant: it’s preserved when the resource is stored.
- `premium_resource_info` (Resource.PremiumResourceInfo): Additional metadata for premium resources from the Content Hub.

## See Also

### Objects
- [object Resource.Base64EncodedResource](./resource.base64encodedresource.md)
  A resource whose bytes are carried as Base64 in the resource itself, so the JSON needs no companion files.
- [object Resource.PremiumResourceInfo](./resource.premiumresourceinfo.md)
  Additional metadata that marks a resource as premium content that the reader originally sourced from the content hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/resource.indirectresource)*