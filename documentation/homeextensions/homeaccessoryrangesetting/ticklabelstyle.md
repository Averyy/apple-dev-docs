# HomeAccessoryRangeSetting.TickLabelStyle

**Framework**: HomeExtensions  
**Kind**: enum  
**Role**: Enumeration

Styles for labeling the tick marks on a stepped slider.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum TickLabelStyle
```

## Overview

Continuous sliders don’t display tick labels.

## Topics

### Label styles
- [HomeAccessoryRangeSetting.TickLabelStyle.automatic](./ticklabelstyle/automatic.md)
  Labels that display each tick mark’s value, using the setting’s decimal precision.
- [HomeAccessoryRangeSetting.TickLabelStyle.custom(_:)](./ticklabelstyle/custom%28_%29.md)
  Custom labels, one for each tick mark.
- [HomeAccessoryRangeSetting.TickLabelStyle.hidden](./ticklabelstyle/hidden.md)
  No tick labels.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Creating a range setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, lowerBound: Value?, upperBound: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,isenabled,defaultvalue,currentvalue,lowerbound,upperbound,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with explicit lower and upper bounds.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting from a range expression.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with symbols at each end of the slider.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?, tickLabelStyle: HomeAccessoryRangeSetting<Value>.TickLabelStyle)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle,ticklabelstyle%29.md)
  Creates a range setting with labeled tick marks.
- [HomeAccessoryRangeSetting.ValueFormat](./valueformat.md)
  Formats that describe the kind of value a range setting represents.
- [HomeAccessoryRangeSetting.SliderStyle](./sliderstyle.md)
  Display styles for a range setting’s slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesetting/ticklabelstyle)*