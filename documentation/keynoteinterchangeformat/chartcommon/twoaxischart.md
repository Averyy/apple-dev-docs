# ChartCommon.twoAxisChart

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A two-axis chart, which is a category chart with two independent value scales.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ChartCommon.twoAxisChart
```

## Overview

The two scales let Keynote measure different series against different value axes. It’s the only chart type that uses `value_axis_secondary`, and, like the mixed chart, it lets each series pick its shape through its `ChartSeries.mixed_series_type` value.

Written as `{"twoAxisChart": …}`: the `twoAxisChart` form of `ChartCommon`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-common`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `twoAxisChart` (TwoAxisChart) *(required)*: A two-axis chart, which is a category chart with two independent value scales. The two scales let Keynote measure different series against different value axes. It’s the only chart type that uses `value_axis_secondary`, and, like the mixed chart, it lets each series pick its shape through its `ChartSeries.mixed_series_type` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartcommon/twoaxischart)*