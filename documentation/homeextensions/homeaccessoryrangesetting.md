# HomeAccessoryRangeSetting

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

A setting that represents a numeric value within a range.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@propertyWrapper
final class HomeAccessoryRangeSetting<Value> where Value : Comparable, Value : Numeric
```

## Overview

The Home app presents this setting as a slider. The slider appears only when the setting has both a lower and an upper bound.

## Topics

### Creating a range setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, lowerBound: Value?, upperBound: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./homeaccessoryrangesetting/init%28id,label,isenabled,defaultvalue,currentvalue,lowerbound,upperbound,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with explicit lower and upper bounds.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./homeaccessoryrangesetting/init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting from a range expression.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./homeaccessoryrangesetting/init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with symbols at each end of the slider.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?, tickLabelStyle: HomeAccessoryRangeSetting<Value>.TickLabelStyle)](./homeaccessoryrangesetting/init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle,ticklabelstyle%29.md)
  Creates a range setting with labeled tick marks.
- [HomeAccessoryRangeSetting.ValueFormat](./homeaccessoryrangesetting/valueformat.md)
  Formats that describe the kind of value a range setting represents.
- [HomeAccessoryRangeSetting.SliderStyle](./homeaccessoryrangesetting/sliderstyle.md)
  Display styles for a range setting’s slider.
- [HomeAccessoryRangeSetting.TickLabelStyle](./homeaccessoryrangesetting/ticklabelstyle.md)
  Styles for labeling the tick marks on a stepped slider.
### Configuring presentation
- [var label: HomeAccessorySettingLabel](./homeaccessoryrangesetting/label.md)
  The label to display for this setting.
- [var isEnabled: Bool](./homeaccessoryrangesetting/isenabled.md)
  A Boolean value that indicates whether people can change the setting.
- [var isHidden: Bool](./homeaccessoryrangesetting/ishidden.md)
  A Boolean value that indicates whether the setting is hidden.
### Accessing the value
- [var wrappedValue: Value?](./homeaccessoryrangesetting/wrappedvalue.md)
  The setting’s current value, or its default value if it has none.
- [var projectedValue: HomeAccessoryRangeSetting<Value>](./homeaccessoryrangesetting/projectedvalue.md)
  The setting itself, which you access with a dollar sign prefix.

## Relationships

### Conforms To
- [HomeAccessorySetting](./homeaccessorysetting.md)
- [Identifiable](../Swift/identifiable.md)

## See Also

### Defining accessory settings
- [protocol HomeAccessorySetting](./homeaccessorysetting.md)
  A type that represents a single accessory setting.
- [struct HomeAccessorySettingLabel](./homeaccessorysettinglabel.md)
  The text that the Home app displays for a setting or an option.
- [class HomeAccessoryEnumSetting](./homeaccessoryenumsetting.md)
  A setting that offers a choice among several options.
- [protocol HomeAccessoryEnumSettingConstant](./homeaccessoryenumsettingconstant.md)
  A type whose cases are the options for an enumeration setting.
- [class HomeAccessoryInformationSetting](./homeaccessoryinformationsetting.md)
  A read-only setting that displays a label and a value.
- [protocol HomeAccessoryRangeSettingDescriptor](./homeaccessoryrangesettingdescriptor.md)
  A type that describes the bounds of a range setting.
- [class HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
  A setting that contains a single line of editable text.
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesetting)*