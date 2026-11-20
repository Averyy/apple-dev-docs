# CorrelationChart.genericCorrelationChart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An object with only the properties of CorrelationChart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CorrelationChart.genericCorrelationChart
```

## Overview

Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `CorrelationChart`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `CorrelationChart`.

Written as `{"genericCorrelationChart": …}`: the `genericCorrelationChart` form of `CorrelationChart`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.correlation-chart`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `genericCorrelationChart` (GenericCorrelationChart) *(required)*: An object with only the properties of CorrelationChart. Every set of shared properties has one, to stand in for an object whose kind isn’t recognized. Nothing in the format has the type `CorrelationChart`, though, so this object never appears in a document; its properties appear only as part of the types that adopt `CorrelationChart`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/correlationchart/genericcorrelationchart)*